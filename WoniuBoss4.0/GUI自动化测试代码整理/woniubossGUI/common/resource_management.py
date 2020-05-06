import time

from util.service import Service
from selenium import webdriver

from util.utility import Utility


class ManageResource:

	def __init__(self,driver,base_config_path):
		self.driver = driver
		Service.open_page(self.driver, base_config_path)
		Service.miss_login(self.driver, base_config_path)
		time.sleep(5)
		self.driver.find_element_by_partial_link_text('资源管理').click()
		time.sleep(5)

	#点击解密按钮
	def click_decrypt_button(self):
		self.driver.find_element_by_css_selector('#btn-decrypt').click()

	#输入二次密码
	def input_second_password(self):
		self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/input').send_keys('woniu123')
		self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[3]/button').click()

	# 点击培训资源
	def click_training_resources(self):
		self.driver.find_element_by_partial_link_text('培训资源').click()

	#点击新增按钮
	def click_add_button(self):
		self.driver.find_element_by_css_selector('button.btn-padding:nth-child(1)').click()

	#输入手机号
	def input_phone(self,resphone):
		rphone = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div[1]/div[1]/div[1]/input')
		Service.send_input(rphone,resphone)
	#输入姓名
	def input_name(self,resname):
		rname = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div[1]/div[1]/div[2]/input')
		Service.send_input(rname,resname)
	#随机选择最新状态
	def select_status(self):
		status_select = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div[1]/div[2]/div[1]/select')
		Service.select_random(status_select)

	#随机选择渠道来源
	def select_source(self):
		source_select = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/form/div[1]/div[5]/div[1]/select')
		Service.select_random(source_select)

	#点击保存按钮
	def click_button(self):
		self.driver.find_element_by_id('addCusBtn').click()

	def do_add(self,resphone,resname):
		self.click_decrypt_button()
		self.input_second_password()
		self.click_training_resources()
		self.click_add_button()
		self.input_phone(resphone)
		self.input_name(resname)
		self.select_status()
		self.select_source()
		self.click_button()

	#查询功能验证
	#输入手机号
	def query_resouce_phone(self,resphone):
		pho = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(1) > input:nth-child(6)')
		Service.send_input(pho,resphone)

	#点击查询
	def click_query(self):
		self.driver.find_element_by_css_selector('button.btn:nth-child(7)').click()

	# 点击跟踪按钮
	def click_track(self):
		self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[15]/button[1]').click()

	#组合查询动作
	def do_query(self,resphone):
		self.click_training_resources()
		self.query_resouce_phone(resphone)
		self.click_query()
		self.click_track()

	#点击跟踪资源
	def click_track_resources(self):
		self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div/ul/li[2]/a').click()

	#随机选择跟踪状态
	def select_new_status(self):
		new = self.driver.find_element_by_id('newStatus')
		Service.select_random(new)

	#随机选择优先级别
	def select_priority(self):
		priority = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div/div[2]/div[1]/div[1]/div/form/div[1]/div[2]/select')
		Service.select_random(priority)

	#随机选择时间
	def input_date(self,next_time):
		Service.remove_readonly(driver,'next_time')
		date_ele = driver.find_element_by_id('next_time')
		Service.send_input(date_ele,next_time)

	#输入跟踪内容
	def input_content(self,content):
		con = self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div/div[2]/div[1]/div[1]/div/form/div[2]/div/textarea')
		Service.send_input(con,content)

	#点击保存按钮
	def click_hold(self):
		self.driver.find_element_by_id('saveTrackingBtn').click()

	#组合跟踪资源的动作
	def do_track_resources(self,resphone,next_time,content):
		self.do_query(resphone)
		self.click_track_resources()
		self.select_new_status()
		self.select_priority()
		#self.input_date(next_time)
		self.input_content(content)
		self.click_hold()

	#点击修改按钮
	def click_modify(self):
		self.driver.find_element_by_css_selector('#personal-table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(15) > button:nth-child(2)').click()

	#修改名字
	def modify_name(self,new_name):
		name = self.driver.find_element_by_xpath('/html/body/div[14]/div/div/form/div/div[1]/div[1]/input')
		Service.send_input(name,new_name)

	#点击保存
	def click_hold_modify(self):
		self.driver.find_element_by_id('alterCusBtn').click()

	#组合修改动作
	def do_modify(self,resphone,new_name):
		self.do_query(resphone)
		self.click_modify()
		self.modify_name(new_name)
		self.click_hold_modify()


	#点击前面的小方框
	def click_box(self):
		self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]/input').click()

	#点击废弃按钮
	def click_discard(self):
		self.driver.find_element_by_id('Discard').click()

	#点击确定按钮
	def click_keep(self):
		self.driver.find_element_by_xpath('/html/body/div[13]/div/div/div[3]/button[2]').click()

	#组合废弃资源动作
	def do_discard(self,resphone):
		self.do_query(resphone)
		self.click_box()
		self.click_discard()
		self.click_keep()

	# 点击分配资源
	def click_allocate_resources(self):
		self.driver.find_element_by_partial_link_text('分配资源').click()

	#点击按比例分配按钮
	def click_prorated_distribution(self):
		self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[3]/button[2]').click()

	#点击确认按钮
	def click_pcommit(self):
		self.driver.find_element_by_xpath('//*[@id="proportion_submit"]').click()

	#点击二次确认
	def click_second_pcommit(self):
		self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button[2]').click()

	#组装按比例分配的动作
	def do_prorated_distribution(self):
		self.click_allocate_resources()
		self.click_prorated_distribution()
		self.click_pcommit()
		self.click_second_pcommit()

	# 点击公共资源
	def click_public_resources(self):
		self.driver.find_element_by_partial_link_text('公共资源').click()
		time.sleep(5)

	#随机选择框框
	def select_box(self):
		import random
		n = random.randint(1,10)
		self.driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/div[1]/div[2]/div[2]/table/tbody/tr[{}]/td[1]/input'.format(n)).click()

	#点击认领按钮
	def click_claim(self):
		self.driver.find_element_by_id('ownCusBtn').click()

	#点击确定按钮
	def click_determine(self):
		self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[3]/button').click()



	#认领资源
	def do_claim(self):
		self.click_public_resources()
		self.select_box()
		self.click_claim()
		self.click_determine()

	# 点击转交资源
	def click_change_resources(self):
		self.driver.find_element_by_partial_link_text('转交资源').click()

	#输入手机号进行查询
	def input_resphone(self,resphone):
		ele = self.driver.find_element_by_css_selector('div.col-lg-12:nth-child(1) > input:nth-child(7)')
		Service.send_input(ele,resphone)

	#点击查询
	def click_cquery(self):
		self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/button').click()

	#选中资源
	def select_res(self):
		self.driver.find_element_by_xpath('//*[@id="transmit-table"]/tbody/tr/td[1]/input').click()

	#选择转交的区域
	def select_region(self):
		reg = self.driver.find_element_by_xpath('//*[@id="regionSelect2"]')
		Service.select_random(reg)

	def select_depart(self):
		depart = self.driver.find_element_by_xpath('//*[@id="deptSelect2"]')
		Service.select_random(depart)

	def select_empn(self):
		emp = self.driver.find_element_by_xpath('//*[@id="empNameSelect2"]')
		Service.select_random(emp)

	def click_submit(self):
		self.driver.find_element_by_id('Submit').click()

	def click_second_submit(self):
		self.driver.find_element_by_xpath('//*[@id="resumeDetails"]/../div[10]/div/div/div[3]/button[2]').click()

	#组合转交资源的动作
	def do_change(self,resphone):
		self.click_change_resources()
		self.input_resphone(resphone)
		self.click_cquery()
		time.sleep(2)
		self.select_res()
		self.select_region()
		self.select_depart()
		self.select_empn()
		self.click_submit()
		self.click_second_submit()





if __name__ == '__main__':
	driver = webdriver.Firefox()
	m = ManageResource(driver,'..\\config\\base.conf')
	#m.do_add('13312121211','xiaobaobao')
	#m.do_track_resources('13312121211','2020-5-30','现在忙')
	#m.do_modify('大侠')
	#m.do_claim()
	m.do_change('13845444444')


