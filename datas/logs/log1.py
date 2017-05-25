# -*- coding:utf-8 -*-

import logging

def ma_fonction():
	logging.error("Ceci est une erreur dans une fonction !")


logging.basicConfig(format = "%(asctime)s - %(filename)s - %(funcName)s \
	(%(lineno)d) - %(levelname)s : %(message)s", level = logging.DEBUG)
logging.critical("Ceci est une erreur critique !")

ma_fonction