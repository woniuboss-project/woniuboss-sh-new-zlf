#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/29 21:14


from selenium.common.exceptions import NoSuchElementException

from util.service import Service
from util.utility import Utility
import time

class classmanager:

    def __init__(self, driver, base_config_path):
        self.driver = driver
        Service.miss_login(self.driver, base_config_path)
        self.driver.find_element_by_partial_link_text('班务管理').click()

    #解密
    def decrypt(self,secondPass):
        self.driver.find_element_by_id('btn-decrypt').click()
        ele = self.driver.find_element_by_name('secondPass')
        Service.send_input(ele,secondPass)
        self.driver.find_element_by_xpath('//div[@id="secondPass-modal"]/div/div/div[3]/button').click()

    #点击请假修改按钮
    def click_edit_leave(self):
        self.driver.find_element_by_xpath('//table[@id="leave-table"]/tbody/tr[1]/td[12]/button[3]').click()

    #输入请假原因
    def input_reason(self,reason):
        ele = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/div[2]/form/div[4]/div/textarea')
        time.sleep(10)
        Service.send_input(ele,reason)

    #输入处理意见
    def input_comment(self,comment):
        ele = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/div[2]/form/div[5]/div/textarea')
        time.sleep(10)
        Service.send_input(ele,comment)

    #点击保存按钮
    def click_save(self):
        self.driver.find_element_by_xpath('//div[@id="modLeave-modal"]/div/div/div[3]/button').click()

    #修改学员请假流程
    def do_edit_leave(self,DATA,secondPass):
        self.decrypt(secondPass)
        self.driver.find_element_by_partial_link_text('学员请假').click()
        self.click_edit_leave()
        self.input_reason(DATA['reason'])
        self.input_comment(DATA['comment'])
        self.click_save()
        content1 = self.driver.find_element_by_xpath('//table[@id="leave-table"]/tbody/tr[1]/td[4]/span').text
        content2 = self.driver.find_element_by_xpath('//table[@id="leave-table"]/tbody/tr[1]/td[5]/span').text
        return  content1,content2
