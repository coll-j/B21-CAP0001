
POSTGRES_URL = '127.0.0.1:5433'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'mostsecurepassword'
POSTGRES_DB = 'bluesclues'


class Config:
    """Base configuration."""
    DEBUG = True
    TESTING = False
    # SQLAlchemy
    uri_template = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'
    SQLALCHEMY_DATABASE_URI = uri_template.format(user=POSTGRES_USER,
                                                  pw=POSTGRES_PASSWORD,
                                                  url=POSTGRES_URL,
                                                  db=POSTGRES_DB)

    # Silence the deprecation warning
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    # production config
    pass


def get_config(env=None):
    # if env is None:
        # try:
            # env = get_env_variable('ENV')
        # except Exception:
    env = 'development'
            # print('env is not set, using env:', env)
        
    if env == 'production':
        return ProductionConfig()
    elif env == 'test':
        return TestConfig()

    return DevelopmentConfig()
