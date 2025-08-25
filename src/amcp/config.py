from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_env: str = "dev"
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    db_host: str = "localhost"
    db_port: int = 5432     # host port from docker-compose
    db_user: str = "amcp"
    db_password: str = "amcp"
    db_name: str = "amcp"

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    @property
    def database_url_async(self) -> str:
        return (
            f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

settings = Settings()
