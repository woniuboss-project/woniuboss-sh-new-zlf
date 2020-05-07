#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/26 14:36

from util.service import Service


class training:

    def __init__(self):
        self.session = Service.get_session()

    #排课
    def add_course(self,URL,test_data):
        return self.session.post(url=URL,data=test_data)

    #修改课程
    def edit_course(self,edit_course_infos):
        return self.session.post(url=edit_course_infos['URL'],data=edit_course_infos['DATA'])

    #指定值班
    def saveDuty(self,saveDuty_infos):
        return self.session.post(url=saveDuty_infos['URL'],data=saveDuty_infos['DATA'])

    #技术面试
    def skills_interview(self,skills_interview_infos):
        return self.session.post(url=skills_interview_infos['URL'],data=skills_interview_infos['DATA'])