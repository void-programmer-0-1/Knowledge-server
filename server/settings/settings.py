from pydantic_settings import BaseSettings

class AppSetting(BaseSettings):
    app_name: str = "Knowledge Base"
    app_version: str = "0.1.0"
    app_description: str = "Notes taking application and sharing Knowledge"


class DatabaseSettings(BaseSettings):
    database_url: str


class GunicornServerSettings(BaseSettings):
    host: str
    port: str
    threads: int
    workers: int
    worker_class: str

    class Config:
        env_file = ".env"

