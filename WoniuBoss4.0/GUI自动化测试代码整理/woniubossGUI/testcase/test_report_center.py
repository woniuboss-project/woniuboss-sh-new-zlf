# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_login
# Description:  
# Author:       Administrator
# Date:         2020/2/10
#-------------------------------------------------------------------------------

# 该模块封装与登录相关的测试

import time,unittest
from parameterized import parameterized
# 获取登录用的测试信息
from common.report_center import ReportCenter
from util.service import Service
from util.utility import Utility

test_config_info = Utility.get_json('..\\config\\lf_testdata.conf')
test_case_info = Utility.get_excel_to_tuple(test_config_info[0])
print('test data====',test_case_info)

class ReportCenterTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = Service.get_driver('..\\config\\base.conf')

		cls.common = ReportCenter(cls.driver,'..\\config\\base.conf')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	@parameterized.expand(test_case_info)
	def test_login(self,expect):
		self.common.do_class('..\\config\\base.conf')
		time.sleep(5)
		ele_str = self.driver.find_element_by_css_selector('.pagination-info').get_attribute('innerText')
		print('ele_str===',ele_str)
		if '显示第 1 到第 2 条记录，总共 2 条记录' in ele_str:
			actual = 'query_success'
		else:
			actual = 'query_fail'
		self.assertEqual(actual, expect)

if __name__ == '__main__':

	unittest.main(verbosity=2)