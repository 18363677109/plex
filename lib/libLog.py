#*********************************************************************
# content   = write loggings into console and files
# version   = 0.0.1
# date      = 2017-01-01
#
# license   = MIT
# copyright = Copyright 2017 Filmakademie Baden-Wuerttemberg, Animationsinstitut
# author    = Alexander Richter <contact@richteralexander.com>
#*********************************************************************
# This source file has been developed within the scope of the
# Technical Director course at Filmakademie Baden-Wuerttemberg.
# http://td.animationsinstitut.de
#*********************************************************************

import os
import sys
import logging
import logging.config


USER = os.getenv('username')

#************************
# CLASS
class ContextFilter(logging.Filter):
    USERS = USER

    def filter(self, record):
        record.user = ContextFilter.USERS
        return True


#************************
# LOGGING
def init(software="default", script="default", level=logging.DEBUG, path="", *args, **kwargs):
    logger = logging.getLogger(script)

    # CHECK path param
    if not path:
        path = ("/").join([get_env('DATA_PATH'), 'user', USER, USER + ".log"])

    create_folder(path)

    info_path, error_path, debug_path = path, path, path

    logging_config = dict(
        version= 1,
        disable_existing_loggers= False,
        formatters= {
            "simple": {
                "format": "%(asctime)s | %(user)-10s | %(module)-10s | %(levelname)-7s - %(lineno)-4d | %(message)s",
                "datefmt":"%d.%m.%Y %H:%M:%S"
            },
            "simpleInfo": {
                "format": "%(asctime)s | %(levelname)-7s | %(user)-10s | %(module)-10s - %(funcName)-18s | %(lineno)-4d | %(message)s",
                "datefmt":"%d.%m.%Y %H:%M:%S"
            },
            "simpleDebug": {
                "format": "%(asctime)s | %(levelname)-7s | %(module)-10s - %(funcName)-18s | %(lineno)-4d | %(message)s",
                "datefmt":"%d.%m.%Y %H:%M:%S"
            },
            "simpleConsole": {
                "format": "%(asctime)s | %(levelname)-7s | %(module)-10s - %(funcName)-16s | %(lineno)-4d | %(message)s",
                "datefmt":"%H:%M:%S"
            }
        }#,

        # handlers= {
        #     "console": {
        #         "class": "logging.StreamHandler",
        #         "level": "DEBUG",
        #         "formatter": "simpleConsole",
        #         "stream": "ext://sys.stdout"
        #     },

        #     "info_file_handler": {
        #         "class": "logging.handlers.RotatingFileHandler",
        #         "level": "INFO",
        #         "formatter": "simpleInfo",
        #         "filename": info_path,
        #         "maxBytes": 10485760,
        #         "backupCount": 20,
        #         "encoding": "utf8"
        #     },

        #     "debug_file_handler": {
        #         "class": "logging.handlers.RotatingFileHandler",
        #         "level": "DEBUG",
        #         "formatter": "simpleInfo",
        #         "filename": debug_path,
        #         "maxBytes": 10485760,
        #         "backupCount": 20,
        #         "encoding": "utf8"
        #     },

        #     "error_file_handler": {
        #         "class": "logging.handlers.RotatingFileHandler",
        #         "level": "ERROR",
        #         "formatter": "simpleDebug",
        #         "filename": error_path,
        #         "maxBytes": 10485760,
        #         "backupCount": 20,
        #         "encoding": "utf8"
        #      }
        # },

        # logger= {
        #     "my_module": {
        #         "level": level,
        #         "handlers": ["console"],
        #         "propagate": "no"
        #     }
        # },

        # root= {
        #     "level": level,
        #     #"handlers": ["console", "info_file_handler", "debug_file_handler", "error_file_handler"]
        # }
    )

    # CONSOLE
    console_handler = logging.StreamHandler(stream=sys.stdout)
    formatter       = logging.Formatter(logging_config["formatters"]["simpleConsole"]["format"], logging_config["formatters"]["simpleConsole"]["datefmt"])
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)

    # DEBUG
    if level == logging.DEBUG:
        debug_handler = logging.handlers.RotatingFileHandler(debug_path, mode='a', maxBytes=10485760, backupCount=20, encoding="utf8")
        formatter     = logging.Formatter(logging_config["formatters"]["simpleDebug"]["format"], logging_config["formatters"]["simpleDebug"]["datefmt"])
        debug_handler.setFormatter(formatter)
        debug_handler.setLevel(level)
        logger.addHandler(debug_handler)

    # INFO, WARNING, ERROR
    else: #level == logging.INFO:
        info_handler = logging.handlers.RotatingFileHandler(info_path, mode='a', maxBytes=10485760, backupCount=20, encoding="utf8")
        formatter    = logging.Formatter(logging_config["formatters"]["simpleInfo"]["format"], logging_config["formatters"]["simple"]["datefmt"])
        info_handler.setFormatter(formatter)
        info_handler.setLevel(level)
        logger.addHandler(info_handler)

    logger.setLevel(level)
    logger.addFilter(ContextFilter())

    return logger

#************************
# FUNCTION
def create_folder(path):
    if len(path.split(".")) > 1:
        path = os.path.dirname(path)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            print("WARNING : Can not create folder : %s"% path)

def get_env(var):
    if os.environ.__contains__(var):
        return os.environ[var].split(';')[0]
    print('ENV doesnt exist: {}'.format(var))
    return ""


#************************
# TEST
def test():
    title = "default"
    LOG1  = init(script=title, logger=logging.getLogger(title))
    LOG1.info("START1")
    print LOG1
    LOG1.debug('Failed')
    LOG1.error('Failed to open file', exc_info=True)

    title = "default_new"
    LOG2  = init(script=title, level=logging.DEBUG, logger=logging.getLogger(title))
    LOG2.info("START2")
    LOG2.debug('Failed')

    try: a()
    except: LOG2.error('Failed to open file', exc_info=True)

    LOG1.info('START1_2')
    print LOG2.warning("START2_SECONDTIME")

    try:
        1/0
    except:
        print ""

# test()
