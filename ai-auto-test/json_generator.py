#!/usr/bin/env python
# coding=utf-8


data = {}
data['hostname'] = '60.205.4.180'
data['port'] = 9010
data['api'] = {}
data['api']['blacklist'] = 'blacklist'

import json
with open('configs/project1.conf', 'w') as f:
    json.dump(data, f, sort_keys=True, indent=4)
