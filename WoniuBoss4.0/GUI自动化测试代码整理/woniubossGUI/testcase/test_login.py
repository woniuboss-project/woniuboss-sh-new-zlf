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
from util.service import Service
from util.utility import Utility

test_config_info = Utility.get_json('..\\config\\testdata.conf')
login_info = Utility.get_excel_to_tuple(test_config_info[0])


# 思路：1.获取测试数据；2.执行每条数据；
# 3.实际结果actual与预期结果进行对比，如果一直证明测试通过，否则测试不通过提交缺陷
# 获取所有的登录用到的测试数据及预期结果
class LoginTest(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.driver = Service.get_driver('..\\config\\base.conf')
		from common.login import Login
		cls.login = Login(cls.driver)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	@parameterized.expand(login_info)
	def test_login(self,uname,upass,vfcode,expect):
		# 将参数重新组织成字典
		login_data = {'username':uname,'password':upass,'verifycode':vfcode}
		self.login.do_login('..\\config\\base.conf',login_data)
		from selenium.webdriver.common.by import By
		if Service.is_element_present(self.driver,By.LINK_TEXT,'注销'):
			actual = 'login-pass'
			self.driver.find_element_by_link_text('注销').click()
		else:
			actual = 'login-fail'
			self.driver.refresh()
		self.assertEqual(actual,expect)


if __name__ == '__main__':

	unittest.main(verbosity=2)