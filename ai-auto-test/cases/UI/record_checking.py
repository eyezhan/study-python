#!/usr/bin/env python
# coding=utf-8

import os
import sys
env_path = os.path.join(os.environ['AI_AUTO_ROOT'], 'cases', 'env')
sys.path.append(env_path)
from libs import quit_test

from selenium import webdriver
import json
import logging
import logging.config
import time
import unittest


class LoginLogout(unittest.TestCase):
    def setUp(self):

        # Configuration
        project = 'project1'
        config_path = os.path.join(os.environ['AI_AUTO_ROOT'], 'configs')
        conf_fn = os.path.join(config_path, '%s.conf' % project)
        self.data = json.load(open(conf_fn, 'r'))

        self.base_url = 'http://%s:%d/index.html' % (self.data['hostname'], self.data['port_front'])
        self.base_url = 'http://%s:%d/index.html' % ('101.200.130.201', 4001)

        self.user_type = 'admin'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)  # 隐性等待时间为30秒
        self.login_url = self.base_url + "#/login"
        self.username = 'T00001'
        #self.username = 'wang'

    def test_search(self):
        test_res = 'PASS'
        comments = ''
        retval = 0

        # Launch webpage of login.
        try:
            d = self.driver
            d.get(self.login_url)
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to launch %s.' % self.login_url
            quit_test(test_res, comments)
            return retval

        # Find username/password input box and enter valid account.
        elements = d.find_elements_by_class_name('input_name')
        for e in elements:
            e.clear()
        elements[0].send_keys(self.username)
        elements[1].send_keys('111111')

        e = d.find_element_by_class_name('login')
        e.click()

        time.sleep(3)
        url = d.current_url
        dst_url = self.base_url + "#/Index/home"
        if url != dst_url:
            retval = -1
            test_res = 'FAIL'
            comments = 'Page does not go to home page.'

        # Filter result by user or group.
        es = d.find_elements_by_class_name('ivu-select-item')
        for i in range(len(es) - 1):
            e = es[len(es) - 1 - i]
            e.click()

        quit_test(test_res, comments)
        return retval

    def test_logout(self):
        comments = ''
        retval = 0

        # Login.
        retval = self.test_login()
        if retval != 0:
            test_res = 'FAIL'
            comments = 'Fail to login.'
            quit_test(test_res, comments)

        try:
            d = self.driver
            e = d.find_element(self.data['user_container_by'], self.data['user_container_value'])
            e.click()
            time.sleep(2)
            e = d.find_element(self.data['logout_by'], self.data['logout_value'])
            e.click()
            time.sleep(2)
            d.switch_to_active_element().click()
            time.sleep(2)
            url = d.current_url
            if url == self.login_url:
                test_res = 'PASS'
            else:
                test_res = 'FAIL'
        except:
            test_res = 'FAIL'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    log_fn = os.path.join('%s.log' % os.path.basename(__file__))
    conf_fn = os.path.abspath(
        os.path.join(
            os.environ['AI_AUTO_ROOT'],
            'configs',
            "logging.json"))
    conf_data = json.load(open(conf_fn, 'r'))
    conf_data['handlers']['file_handler']['filename'] = log_fn
    logging.config.dictConfig(conf_data)
    logger = logging.getLogger()

    suite = unittest.TestSuite()
    suite.addTest(LoginLogout("test_search"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
