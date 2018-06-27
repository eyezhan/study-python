#!/usr/bin/env python
# coding=utf-8


import logging


def quit_test(log, test_res, comments=''):
    logging.debug('Test Result: %s' % test_res)
    logging.debug('Comments: %s' % comments)
