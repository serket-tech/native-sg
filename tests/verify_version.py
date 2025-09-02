import sys

import native_sg

if __name__ == "__main__":

    ci_version = sys.argv[1]
    if ci_version == native_sg.__version__:
        sys.exit(0)
    else:
        print(f"wrong version definition:\nCI version: {ci_version}\nnative_sg.__version__: {native_sg.__version__}")
        sys.exit(1)
