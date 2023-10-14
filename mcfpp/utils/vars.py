def get_var(var, default):
    if var is None:
        return default
    return var


def is_variable(value) -> bool:
    return type(value).__name__ not in ["staticmethod", "classmethod", "function"]


def is_builtin(name: str) -> bool:
    return name in ["__module__", "__doc__"]


def is_method(value) -> bool:
    return not is_variable(value)
