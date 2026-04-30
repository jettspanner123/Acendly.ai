from constants.EnviornmentCON import EnvironmentCON


class EnvironmentVariableValidator:

    @staticmethod
    def validate_env_variables():
        if EnvironmentCON.DATABASE_URL is None:
            raise ValueError("DATABASE_URL environment variable is not set.")
        if EnvironmentCON.DATABASE_USER is None:
            raise ValueError("DATABASE_USER environment variable is not set.")
        if EnvironmentCON.DATABASE_PASSWORD is None:
            raise ValueError("DATABASE_PASSWORD environment variable is not set.")
        if EnvironmentCON.DATABASE_NAME is None:
            raise ValueError("DATABASE_NAME environment variable is not set.")