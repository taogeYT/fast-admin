from appboot.apps import BaseAppConfig


class AuthConfig(BaseAppConfig):
    name: str = 'auth'

    class Config:
        env_prefix = 'auth_'


config = AuthConfig()