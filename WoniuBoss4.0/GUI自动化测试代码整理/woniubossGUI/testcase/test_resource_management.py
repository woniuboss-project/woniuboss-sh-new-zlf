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
from common.resource_management import ManageResource
from util.service import Service
from util.utility import Utility

test_config_info = Utility.get_json('..\\config\\cxx_testdata.conf')
#print(test_config_info)
test_add_info = Utility.get_excel_to_tuple(test_config_info[3])
print('test data====',test_add_info)
test_track_info = Utility.get_excel_to_tuple(test_config_info[4])
test_track_resources_info = Utility.get_excel_to_tuple(test_config_info[5])
test_modify_info = Utility.get_excel_to_tuple(test_config_info[6])
test_discard_info = Utility.get_excel_to_tuple(test_config_info[7])
test_prorated_distribution_info = Utility.get_excel_to_tuple(test_config_info[8])
test_claim_info = Utility.get_excel_to_tuple(test_config_info[9])
test_change_info = Utility.get_excel_to_tuple(test_config_info[10])



class MarketTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = Service.get_driver('..\\config\\base.conf')
		cls.common = ManageResource(cls.driver,'..\\config\\base.conf')

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	#新增按钮的验证
	@parameterized.expand(test_add_info)
	def test_resource_add(self,resphone,resname,expect):
		self.common.do_add(resphone,resname)
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('/html/body/div[14]/div/div/div[2]/div').text
		print(ele_str)
		if '新增成功.' in ele_str:
			actual = 'add success'
		else:
			actual = 'add fail'
		self.assertEqual(actual, expect)

	#查询的验证
	@parameterized.expand(test_track_info)
	def test_resource_track(self, expect):
		self.common.do_query('..\\config\\base.conf')
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div/div[2]/div[2]/div/div[2]/div[2]/blockquote/p[1]/span').text
		print('ele_str===', ele_str)
		if '13312121211' in ele_str:
			actual = 'query ok'
		else:
			actual = 'query fail'
		self.assertEqual(actual, expect)

	#新增跟踪信息的验证
	@parameterized.expand(test_track_resources_info)
	def test_track_resource_add(self,resphone,next_time,content,expect):
		self.common.do_track_resources(resphone,next_time,content)
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('').text
		print(ele_str)
		if '新增成功.' in ele_str:
			actual = 'add success'
		else:
			actual = 'add fail'
		self.assertEqual(actual, expect)

	# 修改的验证
	@parameterized.expand(test_modify_info)
	def test_track_modify(self, resphone,new_name, expect):
		self.common.do_modify(resphone,new_name)
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('').text
		print(ele_str)
		if '修改成功.' in ele_str:
			actual = 'modify success'
		else:
			actual = 'modify fail'
		self.assertEqual(actual, expect)

	# 废弃资源的验证
	@parameterized.expand(test_discard_info)
	def test_track_discard(self, resphone, expect):
		self.common.do_discard(resphone)
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('').text
		print(ele_str)
		if '废弃资源成功.' in ele_str:
			actual = 'discard success'
		else:
			actual = 'discard fail'
		self.assertEqual(actual, expect)

	# 等比例分配资源的验证
	@parameterized.expand(test_prorated_distribution_info)
	def test_prorated_distribution(self,expect):
		self.common.do_prorated_distribution()
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div').text
		print(ele_str)
		if '分配完成.' in ele_str:
			actual = 'distribution success'
		else:
			actual = 'distribution fail'
		self.assertEqual(actual, expect)

	# 公共池认领资源的验证
	@parameterized.expand(test_claim_info)
	def test_claim(self, expect):
		self.common.do_claim()
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('').text
		print(ele_str)
		if '认领成功.' in ele_str:
			actual = 'claim success'
		else:
			actual = 'claim fail'
		self.assertEqual(actual, expect)

	# 转交资源的验证
	@parameterized.expand(test_change_info)
	def test_change(self,resphone,expect):
		self.common.do_change()
		time.sleep(5)
		ele_str = self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div').text
		print(ele_str)
		if '转交资源完成.' in ele_str:
			actual = 'change ok'
		else:
			actual = 'change fail'
		self.assertEqual(actual, expect)





if __name__ == '__main__':
	unittest.main(verbosity=2)