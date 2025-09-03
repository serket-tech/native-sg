import subprocess
import shutil
import os
from pathlib import Path
import datetime

# --- CONFIGURATION ---
# Get the directory where the script is located (scripts/)
SCRIPT_DIR = Path(__file__).parent
# Get the project root (one level up)
PROJECT_ROOT = SCRIPT_DIR.parent

# Define paths relative to the project root
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE_PATH = LOG_DIR / "test_failures.log"
DATA_DIR = PROJECT_ROOT / "data"

# Add or remove directories you want to clean after each test run.
ARTIFACT_DIRS = [
    Path.home() / ".pyenv" / "checkpoints",
    DATA_DIR,
    Path.home() / ".cache" / "torch",
    Path.home() / ".cache" / "DataGradients",
]

# Add any pytest arguments you need, like ignoring specific tests.
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

    for dir_path in ARTIFACT_DIRS:
        os.makedirs(dir_path, exist_ok=True)


def main():
    """Main function to collect, run, and clean up tests."""
    # 1. Prepare the log file
    LOG_DIR.mkdir(exist_ok=True)
    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE_PATH, "w") as f:
        f.write(f"Test Failure Log - Run at: {start_time}\n")
        f.write("=" * 80 + "\n\n")

    # 2. Get a list of all tests
    print("Collecting all tests...")
    collect_command = ["pytest", "--collect-only", "-q"] + PYTEST_ARGS
    result = subprocess.run(collect_command, capture_output=True, text=True, cwd=PROJECT_ROOT)

    if result.returncode != 0 and "no tests collected" not in result.stdout:
         print("Pytest collection failed. Error:")
         print(result.stderr)
         return

    test_ids = [
        line.strip()
        for line in result.stdout.splitlines()
        if "::" in line and not line.startswith("=")
    ]
    total_tests = len(test_ids)
    print(f"Collected {total_tests} tests.\n")

    failed_tests = []
    
    # 3. Loop through and run each test
    for i, test_id in enumerate(test_ids):
        print(f"--- [{i+1}/{total_tests}] Running test: {test_id} ---")

        run_command = ["pytest", "-v"] + PYTEST_ARGS + [test_id] # Added -v for more verbose output
        run_result = subprocess.run(
            run_command,
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT
        )

        # 4. Check the result and log failures
        if run_result.returncode != 0:
            print(f"!!! FAILED: {test_id} !!!\n")
            failed_tests.append(test_id)
            
            # CHANGE: Log stdout, which contains the full pytest failure report
            with open(LOG_FILE_PATH, "a") as f:
                f.write(f"--- FAILED: {test_id} ---\n\n")
                f.write(run_result.stdout) # This contains the failure reason
                if run_result.stderr:
                    f.write("\n--- STDERR ---\n")
                    f.write(run_result.stderr)
                f.write("\n" + "=" * 80 + "\n\n")
        else:
            print(f"--- PASSED: {test_id} ---\n")

        # 5. Clean up artifacts after every run
        cleanup_artifacts()
        print("-" * 80)

    # 6. Print the final summary
    print("\n" + "=" * 80)
    print("TEST RUN COMPLETE")
    print("=" * 80)

    if failed_tests:
        print(f"\nThe following {len(failed_tests)} tests failed:")
        for test in failed_tests:
            print(f" - {test}")
        print(f"\nDetailed error messages have been saved to: {LOG_FILE_PATH}")
    else:
        print("\nAll collected tests passed successfully!")


if __name__ == "__main__":
    main()