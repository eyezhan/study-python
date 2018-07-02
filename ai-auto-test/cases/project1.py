#!/usr/bin/env python
# coding=utf-8


from libs import *
import logging
import argparse
import json
import os
import requests
import sys
import time


# Configuration
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
conf_fn = os.path.join(root_dir, 'configs', '%s.conf' % os.path.splitext(os.path.basename(__file__))[0])
data = json.load(open(conf_fn, 'r'))

URL = 'http://%s:%d' % (data['hostname'], data['port'])
API = data['api']
HEADERS = {'Accept': 'application/json'}


#def play_audio()
#

# Blacklist Controller
#def delete_blacklist()
#
#def get_blacklist()
#
def add_blacklist(data_lst):
    '''
    Test for POST /api/blacklist/add
    '''

    url = '%s/api/%s/add' % (URL, API['blacklist'])
    logging.info(url)
    try:
        r = requests.post(url, headers=HEADERS, json=data_lst)

        return r

    except Exception, e:
        logging.error(e)
        return None


#def download_blacklist_template()
#
#def export_blacklist()
#
#def import_blacklist()
#
#def delete_blacklist_by_id()


def get_blacklist_call_results(*mobile):
    '''
    Test for GET /api/blacklist and /api/blacklist/{mobile}
    '''

    comments = ''
    url = '%s/api/%s' % (URL, API['blacklist'])
    print url
    if mobile:
        url += '/%s' % mobile
    logging.info(url)

    r = get_api(url)

    return r


if __name__ == '__main__':
    from pprint import pprint
    #single_account = [
    #    {
    #        "name": "彭程",
    #        "sex": 1,
    #        "mobile": "15711362928"
    #    }
    #]

    #multi_accounts = [
    #    {
    #        "name": "name",
    #        "sex": 1,
    #        "mobile": "15711362928"
    #    },
    #    {
    #        "name": "名字",
    #        "sex": 0,
    #        "mobile": "12345678901"
    #    }
    #]

    #r = add_blacklist(single_account)
    #r = add_blacklist(multi_accounts)
    r = get_blacklist_call_results('15711362928')
    #r = get_blacklist_call_results('25711362928')

    if r is None:
        sys.exit(-1)

    pprint(r.json())
