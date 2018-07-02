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


# Audio Controller
def play_audio(attach_id):
    '''
    Test for GET /api/audio/{attachId}.
    Play audio {attachId}.
    '''

    url = '%s/api/%s/%s' % (URL, API['audio'], attach_id)

    r = get_api(url)

    return r


# Blacklist Controller
def get_blacklist(url):
    '''
    Test for GET /api/blacklist.
    Get blacklist when assigning page number and page size.
    '''

    r = get_api(url)

    return r


def add_blacklist(data_lst):
    '''
    Test for POST /api/blacklist/add.
    '''

    url = '%s/api/%s/add' % (URL, API['blacklist'])

    r = post_api(url, json=data_lst)

    return r


def download_blacklist_template():
    '''
    Test for GET /api/blacklist/downloadTemplate.
    Download blacklist template.
    '''

    url = '%s/api/%s/downloadTemplate' % (URL, API['blacklist'])

    r = get_api(url, headers={"Accept": "application/vnd.ms-excel"})

    return r


#def export_blacklist()
#
#def import_blacklist()
#
def delete_blacklist_by_ids(data_lst):
    '''
    Test for DELETE /api/blacklist and /api/blacklist/{mobile}.
    Get blacklist call results by mobile.
    '''

    url = '%s/api/%s' % (URL, API['blacklist'])

    r = delete_api(url, json=data_lst)

    return r


def get_blacklist_call_results(mobile):
    '''
    Test for GET /api/blacklist and /api/blacklist/{mobile}.
    Get blacklist call results by mobile.
    '''

    url = '%s/api/%s/%s' % (URL, API['blacklist'], mobile)

    r = get_api(url)

    return r


# Call Recoed Controller
def get_call_record_by_call_id(call_id):
    '''
    Test for GET /api/callRecord/{callId}.
    '''

    url = '%s/api/%s/%s' % (URL, API['callRecord'], call_id)

    r = get_api(url)

    return r


# Call Task Controller
def delete_call_task_by_ids(data_lst):
    '''
    Test for DELETE /api/callTask.
    Delete call task by ids.
    '''

    url = '%s/api/%s' % (URL, API['callTask'])

    r = delete_api(url, json=data_lst)

    return r


# Login Controller
def login(url):
    '''
    Test for POST /api/login.
    '''

    r = post_api(url)

    return r


def logout():
    '''
    Test for GET /api/logout.
    '''

    url = '%s/api/%s' % (URL, API['logout'])

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
    #r = get_blacklist_call_results('15711362928')
    #r = get_blacklist_call_results('25711362928')

    #url = '%s/api/%s' % (URL, API['blacklist'])
    #url += '?pageNo=1&pageSize=20'
    #r = get_blacklist(url)

    #ids = ["12345", "67890"]
    #r = delete_blacklist_by_ids(ids)

    #r = download_blacklist_template()
    #print r

    #url = '%s/api/%s' % (URL, API['login'])
    #email = 'admin'
    #password = '123'
    #url += '?email=%s&password=%s' % (email, password)
    #r = login(url)

    #r = logout()

    #r = play_audio("1")

    #r = get_call_record_by_call_id("1")

    ids = ["1", "2"]
    r = delete_call_task_by_ids(ids)

    if r is None:
        sys.exit(-1)

    pprint(r.json())
    #print r.status_code
