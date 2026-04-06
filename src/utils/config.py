from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    PORT: int
    DATABASE_URL: str

    model_config = SettingsConfigDict(env_file=".env")


Settings = Config()