from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    PORT: int
    DATABASE_URL: str

    # JWT settings
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    model_config = SettingsConfigDict(env_file=".env")


Settings = Config()