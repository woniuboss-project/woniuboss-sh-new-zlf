# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         test_login
# Description:  
# Author:       Administrator
# Date:         2020/2/10
#-------------------------------------------------------------------------------

# 该模块封装与市场营销相关的测试

import time,unittest
from parameterized import parameterized
# 获取登录用的测试信息
from common.market import Market
from util.service import Service
from util.utility import Utility

test_config_info = Utility.get_json('..\\config\\cxx_testdata.conf')
print(test_config_info)
test_query_info = Utility.get_excel_to_tuple(test_config_info[0])
print('test data====',test_query_info)
test_add1_info = Utility.get_excel_to_tuple(test_config_info[1])
print('test data====',test_add1_info)
test_add2_info = Utility.get_excel_to_tuple(test_config_info[2])
class MarketTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = Service.get_driver('..\\config\\base.conf')
		cls.common = Market(cls.driver,'..\\config\\base.conf')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	'''
	@parameterized.expand(test_query_info)
	def test_market(self,expect):
		self.common.do_query('..\\config\\base.conf')
		time.sleep(5)
		ele_str = self.driver.find_element_by_css_selector('.pagination-info').get_attribute('innerText')
		print('ele_str===',ele_str)
		if '显示第 1 到第 10 条记录，总共 62 条记录' in ele_str:
			actual = 'query ok'
		else:
			actual = 'query fail'
		self.assertEqual(actual, expect)
	'''

	@parameterized.expand(test_add1_info)
	def test_market_add1(self,cusphone,cusname,expect):
		self.common.do_add1(cusphone,cusname)
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div').text
		print(ele_str)
		if '保存成功，系统已发送邮件通知咨询师' in ele_str:
			actual = 'add success'
		else:
			actual = 'add fail'
		self.assertEqual(actual, expect)

	@parameterized.expand(test_add2_info)
	def test_market_add2(self, expect):
		self.common.do_add2(r'E:\three\一组测试\测试版4.0\专属简历模板.xls')
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div[2]/div').text
		print(ele_str)
		if '总共上传:21 有效数量:20 数据库重复数量:20  存入数量0' in ele_str:
			actual = 'add success'
		else:
			actual = 'add fail'
		self.assertEqual(actual, expect)


if __name__ == '__main__':
	unittest.main(verbosity=2)