#!/usr/bin/env python
# coding=utf-8


data = dict()
data['hostname'] = '60.205.4.180'
data['port'] = 9010
data['api'] = {}
data['api']['blacklist'] = 'blacklist'
data['api']['audio'] = 'audio'
data['api']['login'] = 'login'
data['api']['logout'] = 'logout'
data['api']['callRecord'] = 'callRecord'
data['api']['callTask'] = 'callTask'

import json
with open('configs/project1.conf', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4)
