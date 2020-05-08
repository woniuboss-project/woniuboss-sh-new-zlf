#!/usr/bin/env python
# -*- coding:utf-8 -*-  

from selenium.webdriver.common.by import By

from parameterized import parameterized
import unittest
import time

# 获取测试数据
from common.student import Student
from util.service import Service
from util.utility import Utility

student_datas = Utility.get_json("../config/lf_testdata.conf")
student_data = Utility.get_excel_to_tuple(student_datas[4])

path = '..\\config\\base.conf'
class TestStudent(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver(path)
        Service.miss_login(self.driver, path)
        self.student = Student(self.driver)
        self.student.click_student_manage_link()

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

    @parameterized.expand(student_data)
    def test_student(self,uname, number,expect):
        contents = {'uanme': uname, 'number': number}
        self.student.excute_student(contents)
        if 'xs' in self.driver.driver.find_element_by_css_selector('driver.find_element_by_css_selector').text:
            actual = 'success'
        else:
            actual = 'error'
        self.assertEqual(actual, expect)
if __name__ == '__main__':
    unittest.main(verbosity=2)