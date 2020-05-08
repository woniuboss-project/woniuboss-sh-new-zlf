#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/29 15:23

import time, unittest
from parameterized import parameterized
from selenium.common.exceptions import NoSuchElementException

from common.training import training
from util.service import Service
from util.utility import Utility

# 获取测试数据
test_infos = Utility.get_json('..\\config\\jtttestdata.conf')
#修改课程测试数据
test_edit_course_infos = Utility.get_excel_to_tup(test_infos[3])



class Training(unittest.TestCase):

    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base.conf')
        self.training=training(self.driver,'..\\config\\base.conf')

    def tearDown(self):
        self.driver.quit()

    #修改课程
    @parameterized.expand(test_edit_course_infos)
    def test_edit_course(self,DATA,expect):
        content1,content2 = self.training.do_edit_course(DATA,'woniu123')
        if content1 == DATA['starttime'] and content2 == DATA['endtime']:
            auctual = 'edit_success'
        else:
            auctual = 'edit_file'
        self.assertEqual(auctual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)