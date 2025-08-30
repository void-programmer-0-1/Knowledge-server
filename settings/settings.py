from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    database_url: str
    app_name: str = "Knowledge API"
    