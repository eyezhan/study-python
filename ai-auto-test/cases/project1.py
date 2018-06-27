#!/usr/bin/env python
# coding=utf-8


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
#def add_blacklist()

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
    if mobile:
        url += '/%s' % mobile
    logging.info(url)

    try:
        r = requests.get(url, headers=HEADERS)

        return r

    except Exception, e:
        logging.error(e)
        return None


if __name__ == '__main__':
    r = get_blacklist_call_results()
    if r is None:
        sys.exit(-1)

    logging.debug(r.json())
