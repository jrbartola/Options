import os


def get_env_variable(name: str) -> str:
    value = os.environ.get(name)
    if value is None:
        raise KeyError(
            f"No environment variable set for key {value}: please add it (contents: {os.environ})"
        )
    return value
