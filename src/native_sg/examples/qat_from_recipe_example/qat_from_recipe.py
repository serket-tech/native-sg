import warnings

if __name__ == "__main__":

    warnings.warn("This script is deprecated and will be removed in the future. Please use `native_sg.qat_from_recipe` instead.", DeprecationWarning)
    from native_sg import qat_from_recipe

    qat_from_recipe.main()
