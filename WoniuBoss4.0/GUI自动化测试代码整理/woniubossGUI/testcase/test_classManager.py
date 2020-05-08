#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/29 21:14
import time, unittest
from parameterized import parameterized
from selenium.common.exceptions import NoSuchElementException

from common.classManager import classmanager
from common.training import training
from util.service import Service
from util.utility import Utility

# 获取测试数据
test_infos = Utility.get_json('..\\config\\jtttestdata.conf')
test_edit_student_leave_infos = Utility.get_excel_to_tup(test_infos[4])



class classManager(unittest.TestCase):

    def setUp(self):
        self.driver = Service.get_driver('..\\config\\base.conf')
        self.classmanager=classmanager(self.driver,'..\\config\\base.conf')

    def tearDown(self):
        self.driver.quit()

    #修改学员请假
    @parameterized.expand(test_edit_student_leave_infos)
    def test_edit_student_leave(self,DATA,expect):
        content1,content2 = self.classmanager.do_edit_leave(DATA,'woniu123')
        print(content1,content2)
        print(DATA['reason'],DATA['comment'])
        if content1 == DATA['reason'] and content2 == DATA['comment']:
            auctual = 'edit_success'
        else:
            auctual = 'edit_fail'
        self.assertEqual(auctual,expect)

if __name__ == '__main__':
    unittest.main(verbosity=2)