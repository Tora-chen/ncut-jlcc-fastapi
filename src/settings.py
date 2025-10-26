from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    authing_client_secret: str = ""

    model_config = SettingsConfigDict(
        env_file="ENV/.env",
        env_file_encoding="utf-8",
    )


settings = Settings()
