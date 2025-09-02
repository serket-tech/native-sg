import warnings

if __name__ == "__main__":

    warnings.warn("This script is deprecated and will be removed in the future. Please use `native_sg.train_from_kd_recipe` instead.", DeprecationWarning)
    from native_sg import train_from_kd_recipe

    train_from_kd_recipe.main()
