#!/usr/bin/env python
# coding=utf-8


import logging
import os


class Logger():
    def __init__(self, log_fn, mode):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        fmt = '%(asctime)s - [%(levelname)s] - %(message)s'
        formatter = logging.Formatter(fmt)

        fh =  logging.FileHandler(log_fn, mode=mode)
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        ch.setLevel(logging.DEBUG)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        self.i('Log: %s' % log_fn)

    def i(self, msg):
        self.logger.info(msg)

    def d(self, msg):
        self.logger.debug(msg)

    def w(self, msg):
        self.logger.warning(msg)

    def e(self, msg):
        self.logger.error(msg)

    def c(self, msg):
        self.logger.critical(msg)


def quit_test(log, test_res, comments=''):
    log.d('Test Result: %s' % test_res)
    log.d('Comments: %s' % comments)


if __name__ == '__main__':
    log_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir, 'logs'))
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_fn = os.path.join(log_path, 'logger.log')
    log = Logger(log_fn)

    log.i('This is a logging info message.')
    log.d('This is a logging debug message.')
    log.w('This is a logging warning message.')
    log.e('This is a logging error message.')
    log.c('This is a logging critical message.')
