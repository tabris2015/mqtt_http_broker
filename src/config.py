from pydantic import BaseSettings


class Settings(BaseSettings):
    K_SERVICE: str = "mqtt_broker"
    K_REVISION: str = "docker"
    LOG_LEVEL: str = "DEBUG"
    PORT: int = 8000
    HOST: str = "0.0.0.0"

    class Config:
        env_file = ".env"


settings = Settings()
