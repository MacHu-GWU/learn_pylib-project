# -*- coding: utf-8 -*-

from loguru import logger


def my_sink_1(message):
    print(f"use my_sink_1 to handle message: {message}, {type(message)}, {message.record}, {type(message.record)}")


def my_sink_2(message):
    print(f"use my_sink_2 to handle message: {message}, {type(message)}, {message.record}, {type(message.record)}")


logger.add(my_sink_1)
logger.add(my_sink_2)

logger.info("Hello, world!")
