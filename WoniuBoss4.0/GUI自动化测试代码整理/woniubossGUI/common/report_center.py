import time

from util.service import Service


class ReportCenter:

	def __init__(self,driver,base_config_path):
		self.driver = driver
		Service.miss_login(self.driver, base_config_path)
		time.sleep(1)
		self.driver.find_element_by_partial_link_text('报表中心').click()

	# 点击教学部
	def click_class_link(self):
		self.driver.find_element_by_partial_link_text('教学部').click()

	def do_class(self,base_config_path):
		self.click_class_link()

