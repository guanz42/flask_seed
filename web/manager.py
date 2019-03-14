import logging
from logging.config import dictConfig

from app import create_app

logging_config = dict(
    version=1,
    formatters={
        'simple': {
            'format': '[%(asctime)s] [%(levelname)-7s] [%(module)s:%(filename)s-%(funcName)s-%(lineno)d] %(message)s'}
    },
    handlers={
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'level': 'DEBUG'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logger.log',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'level': 'DEBUG',
            'formatter': 'simple',
            'encoding': 'utf8'
        }
    },

    root={
        'handlers': ['console', 'file'],
        'level': logging.DEBUG,
    },
)

dictConfig(logging_config)

app = create_app()

if __name__ == '__main__':
    app.run()
