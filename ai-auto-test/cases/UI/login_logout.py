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

        self.user_type = 'admin'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)  # 隐性等待时间为30秒
        self.login_url = self.base_url + "#/login"

    def test_login(self):
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
        for element in ['username', 'password']:
            try:
                e = d.find_element(self.data['%s_by' % element], self.data['%s_value' % element])
            except:
                retval = -1
                test_res = 'FAIL'
                comments = 'Fail to find element %s.' % element
                quit_test(test_res, comments)
                return retval
            else:
                try:
                    e.clear()
                    e.send_keys(self.data['%s_%s' % (element, self.user_type)])
                except:
                    retval = -1
                    test_res = 'FAIL'
                    comments = 'Fail to input %s.' % element
                    quit_test(test_res, comments)
                    return retval

        # Find "Sign In" button and click.
        try:
            e = d.find_element(self.data['sign_in_by'], self.data['sign_in_value'])
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to find "Sign In" button.'
            quit_test(test_res, comments)
            return retval
        else:
            e.click()

        time.sleep(3)
        url = d.current_url
        dst_url = self.base_url + "#/systemManage/profile"
        if url != dst_url:
            retval = -1
            test_res = 'FAIL'
            comments = 'Page does not go to profile page of system management.'
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
    suite.addTest(LoginLogout("test_login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
