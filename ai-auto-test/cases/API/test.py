#!/usr/bin/env python
# coding=utf-8


from libs import quit_test
from project1 import get_blacklist_call_results
import argparse
import json
import logging
import logging.config
import os
import requests
import sys


def test(**kwargs):
    url = 'http://60.205.4.180:9010/api/blacklist/add'
    if kwargs:
        for i in kwargs:
            print i, kwargs[i]
            url += '/%s' % i
    print url


def add_blacklist(url, **kwargs):
    '''
    Test for POST /api/blacklist/add
    '''

    try:
        r = requests.post(url, **kwargs)

        return r

    except Exception, e:
        print e
        return None


if __name__ == '__main__':
    d = {}
    d['url'] = 'http://baidu.com'
    kwargs = {}
    test(json=d, file=2)
    sys.exit()

    single_account = [
        {
            "name": "彭程",
            "sex": 1,
            "mobile": "15711362928"
        }
    ]
    url = 'http://60.205.4.180:9010/api/blacklist/add'

    r = add_blacklist(url, json=single_account)
    if r is None:
        sys.exit(-1)

    print r.json()
