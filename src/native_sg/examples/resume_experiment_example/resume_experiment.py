import warnings

if __name__ == "__main__":

    warnings.warn("This script is deprecated and will be removed in the future. Please use `native_sg.resume_experiment` instead.", DeprecationWarning)
    from native_sg import resume_experiment

    resume_experiment.main()
