'''
========================== CONSTANTS ==========================

This file contains some constants methods and features to easier your ML developement

Some classes here:
    - Logs
'''

'''
========================== CONSTANTS ==========================

This file contains some constants methods and features to easier your ML developement

Some classes here:
    - Logs
'''

import os

class Logs:
    @staticmethod
    def config_logging(log_file=None, log_level=logging.INFO):
        '''
        Configures logging and structlog.
        
        :param log_file: Path to the log file (optional).
        :param log_level: Logging level (default is INFO).
        '''
        import structlog
        import logging
        from logging import StreamHandler

        handlers = [StreamHandler()]
        if log_file:
            handlers.append(logging.FileHandler(log_file))

        logging.basicConfig(
            level=log_level,
            format="%(message)s",
            handlers=handlers
        )

        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.JSONRenderer()
            ],
            logger_factory=structlog.stdlib.LoggerFactory(),
            wrapper_class=structlog.stdlib.BoundLogger,
            cache_logger_on_first_use=True,
        )

class Paths:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    MODELS_DIR = os.path.join(BASE_DIR, 'models')
    LOGS_DIR = os.path.join(BASE_DIR, 'logs')

    @staticmethod
    def ensure_dirs_exist():
        '''
        Creates required directories if they do not exist.
        '''
        for path in [Paths.DATA_DIR, Paths.MODELS_DIR, Paths.LOGS_DIR]:
            os.makedirs(path, exist_ok=True)
