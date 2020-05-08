#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/29 15:23

from selenium.common.exceptions import NoSuchElementException

from util.service import Service
from util.utility import Utility
import time

class training:

    def __init__(self, driver, base_config_path):
        self.driver = driver
        Service.miss_login(self.driver, base_config_path)
        self.driver.find_element_by_partial_link_text('教学管理').click()

    def decrypt(self,secondPass):
        self.driver.find_element_by_id('btn-decrypt').click()
        ele = self.driver.find_element_by_name('secondPass')
        Service.send_input(ele,secondPass)
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div/div/div[3]/button').click()

    #点击修改按钮
    def click_edit_course(self):
        self.driver.find_element_by_xpath('//table[@id="course_table"]/tbody//tr[1]/td[9]/button').click()


    #选择课程开始时间
    def select_start_time(self,s_time):
        js1 = f'document.querySelector("div.col-sm-6:nth-child(1) > input:nth-child(2)").value="{s_time}";'
        #div.col-sm-6:nth-child(1) > input:nth-child(2)
        js2 = 'document.querySelector("body > div:nth-last-child(7) > div.datetimepicker-days").style="display: none;"'
        js3 = 'document.querySelector.("body > div:nth-last-child(7)")style = "display: none;"'
        self.driver.execute_script(js2)
        self.driver.execute_script(js3)
        self.driver.execute_script(js1)

    #选择课程结束时间
    def select_end_time(self,e_time):
        js1 = f'document.querySelector("div.col-sm-6:nth-child(2) > input:nth-child(2)").value="{e_time}";'
        js2 = 'document.querySelector("body > div:nth-last-child(6) > div.datetimepicker-days").style="display: none;"'
        js3 = 'document.querySelector("body > div:nth-last-child(6)").style = "display: none;"'
        self.driver.execute_script(js2)
        self.driver.execute_script(js3)
        self.driver.execute_script(js1)

    #点击保存按钮
    def click_save_button(self):
        self.driver.find_element_by_xpath('//div[@id="modifyCourse"]/div/div/div[2]/button').click()

    #修改排课流程
    def do_edit_course(self,DATA,secondPass):
        self.decrypt(secondPass)
        self.driver.find_element_by_partial_link_text('课程安排').click()
        self.click_edit_course()
        self.select_start_time(DATA['starttime'])
        self.select_end_time(DATA['endtime'])
        self.click_save_button()
        content1 = self.driver.find_element_by_xpath('//table[@id="course_table"]/tbody/tr[1]/td[7]').text
        content2 = self.driver.find_element_by_xpath('//table[@id="course_table"]/tbody/tr[1]/td[8]').text
        return  content1,content2










