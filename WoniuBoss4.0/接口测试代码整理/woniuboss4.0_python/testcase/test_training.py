#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/26 14:37

import requests,time
import unittest
from parameterized import parameterized

from common.student import student
from common.training import training
from util.utility import Utility
#基本信息
test_infos=Utility.get_json('..\\config\\jtttestdata.conf')
#排课测试数据
test_add_course_infos=Utility.get_excel_to_tuple(test_infos[5])
#教师课程修改测试数据
test_edit_course_infos=Utility.get_excel_to_tuple(test_infos[6])
#指定值班测试数据
test_saveDuty_infos=Utility.get_excel_to_tuple(test_infos[7])
#申请加班测试数据
test_saveApply_infos=Utility.get_excel_to_tuple(test_infos[8])
#技术面试测试数据
test_skills_interview_infos=Utility.get_excel_to_tuple(test_infos[9])



class Training(unittest.TestCase):

    #排课
    @parameterized.expand(test_add_course_infos)
    def test_add_course(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        arr=[DATA['arr']]
        test_data={'arr':arr,'startTime': DATA['startTime'],'endTime': DATA['endTime']}
        resp = training().add_course(URL,test_data)
        self.assertEqual(resp.text,CONTENT)


    #修改排课
    @parameterized.expand(test_edit_course_infos)
    def test_edit_course(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        edit_course_infos={'URL':URL,'DATA':DATA}
        resp = training().edit_course(edit_course_infos)
        print(resp.text)
        self.assertEqual(resp.text,CONTENT)


    #指定教师值班
    @parameterized.expand(test_saveDuty_infos)
    def test_saveDuty(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        saveDuty_infos={'URL':URL,'DATA':DATA}
        resp = training().edit_course(saveDuty_infos)
        self.assertEqual(resp.text,CONTENT)

    #指定教师值班
    @parameterized.expand(test_saveApply_infos)
    def test_saveApply(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        saveApply_infos={'URL':URL,'DATA':DATA}
        resp = training().edit_course(saveApply_infos)
        self.assertEqual(resp.text,CONTENT)


    #技术面试
    @parameterized.expand(test_skills_interview_infos)
    def test_skills_interview(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        skills_interview_infos={'URL':URL,'DATA':DATA}
        resp = training().skills_interview(skills_interview_infos)
        self.assertEqual(resp.text,CONTENT)

if __name__ == '__main__':
    unittest.main(verbosity=2)