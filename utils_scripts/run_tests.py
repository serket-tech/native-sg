import subprocess
import shutil
import os
from pathlib import Path
import datetime
import argparse

# --- CONFIGURATION ---
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
LOG_DIR = PROJECT_ROOT / "logs"
DATA_DIR = PROJECT_ROOT / "data"

ARTIFACT_DIRS = [
    Path.home() / ".pyenv" / "checkpoints",
    DATA_DIR,
    Path.home() / ".cache" / "torch",
    Path.home() / ".cache" / "DataGradients",
]

PYTEST_ARGS = [
    "--ignore=tests/integration_tests/conversion_callback_test.py",
    "--ignore=tests/integration_tests/deci_lab_export_test.py",
]
# --- END CONFIGURATION ---

def cleanup_artifacts():
    """Safely removes the contents of specified artifact directories."""
    print("   -> Cleaning up artifact directories...")
    for dir_path in ARTIFACT_DIRS:
        if dir_path.exists() and dir_path.is_dir():
            try:
                shutil.rmtree(dir_path)
                print(f"      - Cleared {dir_path}")
            except OSError as e:
                print(f"      - Error clearing {dir_path}: {e}")
    # for dir_path in ARTIFACT_DIRS:
    #     os.makedirs(dir_path, exist_ok=True)

def write_to_log_and_stdout(message, log_file_path):
    """Prints a message to the console and appends it to the log file."""
    print(message)
    with open(log_file_path, "a") as f:
        f.write(message + "\n")

def run_single_test(test_id, log_file_path):
    """Runs a single pytest test, logs the result, and returns the exit code."""
    run_command = ["pytest", "-v"] + PYTEST_ARGS + [test_id]
    run_result = subprocess.run(
        run_command,
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT
    )

    if run_result.returncode != 0:
        with open(log_file_path, "a") as f:
            f.write(f"--- FAILED: {test_id} ---\n\n")
            f.write(run_result.stdout)
            if run_result.stderr:
                f.write("\n--- STDERR ---\n")
                f.write(run_result.stderr)
            f.write("\n" + "=" * 80 + "\n\n")
            
    return run_result.returncode

def main():
    """Parses arguments and runs the test suite."""
    parser = argparse.ArgumentParser(description="Run the super-gradients test suite with artifact cleanup.")
    parser.add_argument("--last-failed", action="store_true", help="Rerun only the tests that failed in the last session.")
    parser.add_argument("--cleanup", action="store_true", help="Cleanup artifact directories before running tests.")
    args = parser.parse_args()

    # 1. Prepare timestamped log file
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    LOG_DIR.mkdir(exist_ok=True)
    log_file_path = LOG_DIR / f"test_run_{timestamp}.log"
    with open(log_file_path, "w") as f:
        f.write(f"Test Run Log - Started at: {timestamp}\n")
        f.write("=" * 80 + "\n\n")

    # 2. Determine which tests to run
    collection_args = ["--collect-only", "-q"]
    if args.last_failed:
        print("Collecting last failed tests...")
        collection_args.append("--last-failed")
    else:
        print("Collecting all tests...")
    
    collect_command = ["pytest"] + collection_args + PYTEST_ARGS
    result = subprocess.run(collect_command, capture_output=True, text=True, cwd=PROJECT_ROOT)
    test_ids = [line.strip() for line in result.stdout.splitlines() if "::" in line and not line.startswith("=")]
    
    if not test_ids:
        message = "No tests to run."
        write_to_log_and_stdout(message, log_file_path)
        return

    total_tests = len(test_ids)
    print(f"Found {total_tests} tests to run.\n")
    failed_tests = []

    # 3. UNIFIED TEST EXECUTION LOOP
    for i, test_id in enumerate(test_ids):
        print(f"--- [{i+1}/{total_tests}] Running test: {test_id} ---")
        
        return_code = run_single_test(test_id, log_file_path)
        
        if return_code != 0:
            print(f"!!! FAILED: {test_id} !!!\n")
            failed_tests.append(test_id)
        else:
            print(f"--- PASSED: {test_id} ---\n")
            
        # Cleanup runs after every test, regardless of mode.
        if args.cleanup:
            cleanup_artifacts()
        print("-" * 80)
        
    # 4. Final Summary
    summary_lines = []
    summary_lines.append("\n" + "="*80)
    summary_lines.append("TEST RUN SUMMARY")
    summary_lines.append("="*80)

    if failed_tests:
        summary_lines.append(f"\nThe following {len(failed_tests)} out of {total_tests} tests failed:")
        for test in failed_tests:
            summary_lines.append(f" - {test}")
    else:
        summary_lines.append(f"\nAll {total_tests} tests passed successfully!")
    
    summary_message = "\n".join(summary_lines)
    write_to_log_and_stdout(summary_message, log_file_path)

if __name__ == "__main__":
    main()