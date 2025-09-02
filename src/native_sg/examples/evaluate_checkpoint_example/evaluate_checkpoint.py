import warnings

if __name__ == "__main__":

    warnings.warn("This script is deprecated and will be removed in the future. Please use `native_sg.evaluate_checkpoint` instead.", DeprecationWarning)
    from native_sg import evaluate_checkpoint

    evaluate_checkpoint.main()
