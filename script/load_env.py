import os

# Envvar names
CI_ENVVAR_NAME = "GENKAIERA_IS_CI"
TEST_ENVVAR_NAME = "GENKAIERA_IS_TEST"

# Priority is from bottom ( index 0 ) to top ( index -1 ).
ENVFILES_TO_LOAD_IN_CI = ["./.env.ci"]
ENVFILES_TO_LOAD_IN_TEST = ["./.env.test"]
ENVFILES_TO_LOAD_IN_LOCAL = ["./.env.example", "./.env.local"]


def parse_0_or_1_envvar(name: str) -> bool:
    envvar = os.environ.get(name, None)

    if envvar:
        try:
            result: bool = bool(int(envvar))

        except (ValueError, TypeError):
            raise RuntimeError(
                "RuntimeError: the value of the CI environment variable must be an integer with value 0 or 1."
            )

        else:
            return result

    # Unreachable, but required for mypy
    return False


def load_dotenv() -> None:
    try:
        import dotenv

    except ImportError:
        raise RuntimeError(
            "RuntimeError: failed to import 'dotenv'.\n"
            "Please install python-dotenv to use this command."
        )

    envfiles_to_load: list[str]

    if parse_0_or_1_envvar(CI_ENVVAR_NAME):
        envfiles_to_load = ENVFILES_TO_LOAD_IN_CI

    else:
        if parse_0_or_1_envvar(TEST_ENVVAR_NAME):
            envfiles_to_load = ENVFILES_TO_LOAD_IN_TEST

        else:
            envfiles_to_load = ENVFILES_TO_LOAD_IN_LOCAL

    for envfile in envfiles_to_load:
        dotenv.load_dotenv(envfile, verbose=True, override=True)
