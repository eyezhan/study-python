#!/usr/bin/env python
# coding=utf-8


import logging
import requests


HEADER = {'Accept': 'application/json'}


def get_api(url, headers=HEADER):
    logging.info(url)
    logging.info(headers)
    try:
        r = requests.get(url, headers=headers)

        return r

    except Exception as e:
        logging.error(e)

        return None


def post_api(url, headers=HEADER, **kwargs):
    logging.info(url)
    logging.info(headers)
    if kwargs:
        logging.info(kwargs)
    try:
        r = requests.post(url, headers=headers, **kwargs)

        return r

    except Exception as e:
        logging.error(e)

        return None


def delete_api(url, headers=HEADER, **kwargs):
    logging.info(url)
    logging.info(headers)
    if kwargs:
        logging.info(kwargs)
    try:
        r = requests.delete(url, headers=headers, **kwargs)

        return r

    except Exception as e:
        logging.error(e)

        return None


def quit_test(test_res, comments=''):
    logging.debug('Test Result: %s' % test_res)
    logging.debug('Comments: %s' % comments)
