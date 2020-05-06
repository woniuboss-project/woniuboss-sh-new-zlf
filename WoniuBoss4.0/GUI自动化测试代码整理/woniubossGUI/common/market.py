import time

from util.service import Service

from selenium import webdriver
class Market:

	def __init__(self,driver,base_config_path):
		self.driver = driver
		Service.open_page(self.driver, base_config_path)
		Service.miss_login(self.driver, base_config_path)
		time.sleep(5)
		self.driver.find_element_by_partial_link_text('市场营销').click()
		time.sleep(5)
		self.driver.find_element_by_partial_link_text('简历资源').click()

	# 点击简历资源
	def click_resume_resources_link(self):
		self.driver.find_element_by_css_selector('#list-2 > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()

	#点击查询按钮
	def click_query_button(self):
		self.driver.find_element_by_css_selector('button.btn:nth-child(6)').click()

	#查询动作组合
	def do_query(self):
		#self.click_resume_resources_link()
		time.sleep(2)
		self.click_query_button()

	#点击新增按钮
	def add1_click(self):
		self.driver.find_element_by_css_selector('button.btn:nth-child(9)').click()
	#随机选择区域
	def select_region(self):
		region_select = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[1]/select')
		Service.select_random(region_select)
	#随机选择部门
	def select_department(self):
		department_select = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[2]/select')
		Service.select_random(department_select)
	#输入电话
	def input_phone(self,cusphone):
		phone = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[3]/input')
		Service.send_input(phone,cusphone)
	#输入姓名
	def input_name(self,cusname):
		cname = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[4]/input')
		Service.send_input(cname,cusname)
	#随机选择性别
	def select_sex(self):
		sex_select = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[5]/select')
		Service.select_random(sex_select)
	#随机选择最新状态
	def select_status(self):
		status_select = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[6]/select')
		Service.select_random(status_select)
	#随机选择渠道来源
	def select_source(self):
		source_select = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[14]/select')
		Service.select_random(source_select)
	#点击保存
	def click_button(self):
		self.driver.find_element_by_id('addCusBtn').click()
	#点击弹窗中的确定按钮
	def click_alert(self):
		print(self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/div').text)
	#增加动作组合
	def do_add1(self,cusphone,cusname):
		#self.click_resume_resources_link()
		#time.sleep(2)
		self.add1_click()
		time.sleep(2)
		self.select_region()
		self.select_department()
		self.input_phone(cusphone)
		self.input_name(cusname)
		self.select_sex()
		self.select_status()
		self.select_source()
		self.click_button()
		self.click_alert()
	#上传简历
	#点击上传按钮
	def add2_click(self):
		self.driver.find_element_by_css_selector('button.btn:nth-child(8)').click()

	# 随机选择区域
	def select_region2(self):
		region_select = self.driver.find_element_by_xpath('//*[@id="regionSelect"]')
		Service.select_random(region_select)

	# 随机选择部门
	def select_department2(self):
		department_select = self.driver.find_element_by_xpath(
			'//*[@id="dpetSelect"]')
		Service.select_random(department_select)

	#上传文件
	def send_up_file(self,path):
		self.driver.find_element_by_xpath('//*[@id="files"]').send_keys(path)

	#点击提交按钮
	def commit_click(self):
		self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[3]/button').click()


	#组合上传动作
	def do_add2(self,path):
		self.add2_click()
		self.select_region2()
		self.select_department2()
		self.send_up_file(path)
		self.commit_click()








if __name__ == '__main__':
	driver = webdriver.Firefox()
	#Market(driver,'..\\config\\base.conf')
	m = Market(driver,'..\\config\\base.conf')
	#m.do_query()
	#m.do_add1('13345678916','xiaowang')
	m.do_add2(r'E:\three\一组测试\测试版4.0\专属简历模板.xls')
