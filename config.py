from pydantic import model_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URL: str = None

    @model_validator(mode="before")
    def get_database_url(cls, v):
        v[
            "DATABASE_URL"] = f"postgresql+asyncpg://{v['DB_USER']}:{v['DB_PASSWORD']}@{v['DB_HOST']}:{v['DB_PORT']}/{v['DB_NAME']}"
        return v

    class Config:
        env_file = ".env"


settings = Settings()
print(settings.DATABASE_URL)
