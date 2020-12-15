# -*- coding: utf-8 -*-
import logging
from logging.handlers import TimedRotatingFileHandler
from options import menu
from simplification import fonctions as f
import os
import errno

if __name__ == '__main__':

    logger = logging.getLogger("cultureg")
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(levelname)s] %(asctime)s -- %(name)s -- %(message)s")

    try:
        os.makedirs(f.chemin_absolu('log'))
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    handler1 = logging.handlers.TimedRotatingFileHandler('log/info.log', when="d", interval=7, encoding="utf-8")
    handler1.setLevel(logging.INFO)
    handler1.setFormatter(formatter)
    logger.addHandler(handler1)
    handler2 = logging.handlers.TimedRotatingFileHandler("log/error.log", when="d", interval=7, encoding="utf-8")
    handler2.setLevel(logging.ERROR)
    handler2.setFormatter(formatter)
    logger.addHandler(handler2)

    menu.lancement_application()
