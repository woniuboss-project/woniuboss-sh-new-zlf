# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         login
# Description:  
# Author:       Administrator
# Date:         2020/2/10
#-------------------------------------------------------------------------------
from util.service import Service

class Login:

	def __init__(self,driver):
		self.driver = driver

	# 向用户名输入框输入内容
	def input_uname(self,username):
		pass

	# 向密码框输入密码
	def input_upass(self,password):
		pass

	# 向验证码框输入验证码
	def input_vfcode(self,verifycode):
		pass

	# 点击登录按钮
	def click_button(self):
		pass

	# 将以上的动作进行组织，形成整体的登录操作,参数login_data是字典
	def do_login(self,base_config_path,login_data):
		pass
