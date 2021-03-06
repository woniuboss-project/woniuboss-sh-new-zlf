# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:         driven
# Description:  
# Author:       Administrator
# Date:         2020/2/13
#-------------------------------------------------------------------------------
import unittest

class Driven:

	def start(self):
		from HTMLTestRunner import HTMLTestRunner
		ts = unittest.TestSuite()
		loader = unittest.TestLoader()
		from guitest.woniusales_test03.util.utility import Utility
		testcase_names = Utility.trans_str('..\\config\\test.conf')
		tests = loader.loadTestsFromNames(testcase_names)
		ts.addTests(tests)
		# 测试报告文件名称的格式为：xxxx-xx-xx_xx_xx_xx_report.html
		import time
		ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
		with open('..\\report\\%s_report.html'%(ctime),'w') as file:
			runner = HTMLTestRunner(stream=file,verbosity=2)
			runner.run(ts)

if __name__ == '__main__':
	Driven().start()
	# import os
	# print(os.path.abspath('.'))
