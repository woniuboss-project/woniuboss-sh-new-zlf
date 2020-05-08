#!/usr/bin/env python
# -*- coding:utf-8 -*-
from util.service import Service


class Student:

    def __init__(self, driver):
        self.driver = driver


    def click_student_manage_link(self):
        self.driver.find_element_by_link_text('学员管理').click()


    def input_name(self,uname):
        u_name=self.driver.find_element_by_css_selector('find_element_by_css_selector')
        Service.send_input(u_name, uname)

    def input_number(self,number):
        n_umber=self.driver.find_element_by_css_selector('div.col-lg-6:nth-child(2) > input:nth-child(2)')
        Service.send_input(n_umber, number)

    def link_inquire(self):
        self.driver.find_element_by_css_selector('div.col-lg-6:nth-child(2) > button:nth-child(3)').click()

    #查询功能实现
    def excute_student(self,contents):
        self.input_name(contents['uanme'])
        self.input_number(contents['number'])
        self.link_inquire()
