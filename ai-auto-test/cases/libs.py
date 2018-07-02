#!/usr/bin/env python
# coding=utf-8


import logging
import requests


def get_api(url):
    try:
        r = requests.get(url)

        return r

    except Exception, e:
        logging.error(e)

        return None


def quit_test(log, test_res, comments=''):
    logging.debug('Test Result: %s' % test_res)
    logging.debug('Comments: %s' % comments)
