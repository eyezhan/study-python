#!/usr/bin/env python
# coding=utf-8

from login_logout import *


class GlobalAnswer(LoginLogout):
    def setUp(self):
        # Configuration
        project = 'project1'
        config_path = os.path.join(os.environ['AI_AUTO_ROOT'], 'configs')
        conf_fn = os.path.join(config_path, '%s.conf' % project)
        self.data = json.load(open(conf_fn, 'r'))

        self.base_url = 'http://%s:%d/index.html' % (self.data['hostname'], self.data['port_front'])

        self.user_type = 'common'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)  # 隐性等待时间为30秒
        self.login_url = self.base_url + "#/login"

    def test_switch_to_global_answer_page(self):
        test_res = 'PASS'
        comments = ''
        retval = 0

        retval = self.test_login()
        if retval != 0:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to login.'
            quit_test(test_res, comments)
            return retval
            
        d = self.driver
        try:
            e = d.find_element(self.data['call_mgt_by'], self.data['call_mgt_value'])
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to find lable of call management.'
            quit_test(test_res, comments)
        else:
            e.click()
            time.sleep(2)

        try:
            e = d.find_element(self.data['call_history_by'], self.data['call_history_value'])
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to find lable of call history page.'
            quit_test(test_res, comments)
        else:
            e.click()
            time.sleep(2)

        try:
            es = d.find_elements(self.data['ch_search_bars_by'], self.data['ch_search_bars_value'])
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to find search bar.'
            quit_test(test_res, comments)
        else:
            es[4].send_keys("0821")
            time.sleep(2)

        try:
            es = d.find_elements(self.data['ch_btns_by'], self.data['ch_btns_value'])
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to find search bar.'
            quit_test(test_res, comments)
        else:
            e = es[0]
            e.click()
            time.sleep(5)

        try:
            es = d.find_elements("class name", "el-table_1_column_14")
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to find column 14 in result table.'
            quit_test(test_res, comments)
        else:
            e = es[1]
            logger.info("\nTime: %s\n" % e.text)
        finally:
            quit_test(test_res, comments)
            return retval


if __name__ == "__main__":
    # Log.
    #log_path = args.log_path
    # if not os.path.exists(log_path):
    #    os.makedirs(log_path)
    #log_fn = os.path.join(log_path, '%s.log' % os.path.basename(__file__))
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
    suite.addTest(GlobalAnswer("test_switch_to_global_answer_page"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
