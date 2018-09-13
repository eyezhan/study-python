#!/usr/bin/env python
# coding=utf-8

from login_logout import *


class GlobalAnswer(LoginLogout):
    def setUp(self):
        super(GlobalAnswer, self).setUp()

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
            e = d.find_element(self.data['conf_mgt_by'], self.data['conf_mgt_value'])
        except:
            retval = -1
            test_res = 'FAIL'
            comments = 'Fail to find lable of configuration management.'
        else:
            e.click()
            time.sleep(3)
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
