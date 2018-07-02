#!/usr/bin/env python
# coding=utf-8


import logging
import requests


def get_api(url):
    logging.info(url)
    try:
        r = requests.get(url)

        return r

    except Exception, e:
        logging.error(e)

        return None


def post_api(url, **kwargs):
    logging.info(url)
    if kwargs:
        logging.info(kwargs)
    try:
        r = requests.post(url, **kwargs)

        return r

    except Exception, e:
        logging.error(e)

        return None


def delete_api(url, **kwargs):
    logging.info(url)
    if kwargs:
        logging.info(kwargs)
    try:
        r = requests.delete(url, **kwargs)

        return r

    except Exception, e:
        logging.error(e)

        return None


def quit_test(test_res, comments=''):
    logging.debug('Test Result: %s' % test_res)
    logging.debug('Comments: %s' % comments)
