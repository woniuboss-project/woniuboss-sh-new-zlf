#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/24 12:18

import requests,time
import unittest
from parameterized import parameterized

from common.student import student
from util.utility import Utility
#基本信息
test_infos=Utility.get_json('..\\config\\jtttestdata.conf')
#学员信息查询测试数据
query_student_infos=Utility.get_excel_to_tuple(test_infos[0])
#学员晨考和作业测试数据
Mornexam_homework_infos=Utility.get_excel_to_tuple(test_infos[1])
#学员周考成绩测试数据
test_upload_weekexam_infos=Utility.get_excel_to_tuple(test_infos[2])
#学员阶段测评测试数据
test_upload_phaseExam_infos=Utility.get_excel_to_tuple(test_infos[3])
#学员综合成绩查询
test_query_comprehensive_infos=Utility.get_excel_to_tuple(test_infos[4])
#学员信息修改测试数
test_edit_student_infos=Utility.get_excel_to_tuple(test_infos[6])




class Student(unittest.TestCase):

    #学员信息查询

    @parameterized.expand(query_student_infos)
    def test_query_student(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        query_infos={'URL':URL,'DATA':DATA}
        resp = student().query_student(query_infos)
        result= resp.json()
        #按班级查询
        if DATA['stuClass'] != '':
            SQL="select s.student_name FROM student AS s,class AS c WHERE s.student_class_id = c.class_id AND c.class_no ='{}'".format(DATA['stuClass'])
            DBresult=Utility.query_all('..\\config\\base.conf',SQL)
        #按学生姓名查询
        else:
            SQL = "select * FROM student AS s,class AS c WHERE s.student_class_id = c.class_id AND s.student_name ='{}'".format(DATA['stuName'])
            DBresult = Utility.query_all('..\\config\\base.conf', SQL)
        print(len(DBresult),result['totalRow'])
        if int(result['totalRow']) == len(DBresult) and result['totalRow'] !=0:
                auctual = 'query_sucess'
        else:
            auctual = 'query_fail'

        #断言
        self.assert_(auctual,expect)

    #学员信息修改
    @parameterized.expand(test_edit_student_infos)
    def test_query_student(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        files = {'stu.student_id': (None,'8'), 'stu.student_name': (None, '王二'),
                 'stu.student_no': (None, 'WNSH202004008'),
                 'class_no': (None, 'WNSHC099'), 'stu.tel': (None, '0'), 'stu.sex': (None, '女'),
                 'stu.status': (None, '02'), 'stu.need_fee': (None, '01'),
                 'stu.QQ': (None, ''), 'stu.source': (None, '04'), 'stu.emergency_person': (None, ''),
                 'stu.emergency_tel': (None, ''), 'stu.school': (None, ''),
                 'stu.education': (None, '03'), 'stu.major': (None, ''), 'stu.IDnumber': (None, ''),
                 'stu.graduation_time': (None, ''), 'stu.age': (None, '')
                 }
        edit_infos={'URL':URL,'files':files}
        resp = student().edit_student(edit_infos)

    #学员日常晨考和作业录入验证
    @parameterized.expand(Mornexam_homework_infos)
    def test_Mornexam_homework(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        testinfos= {'URL':URL,'DATA':DATA}
        resp = student().Mornexam_homework(testinfos)
        #断言
        self.assert_(resp.text,CONTENT)

    #周考成绩上传测试
    @parameterized.expand(test_upload_weekexam_infos)
    def test_upload_weekexam(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        upload_weekexam_infos= {'URL':URL,'DATA':DATA}
        resp = student().upload_weekexam(upload_weekexam_infos)
        #断言
        self.assert_(resp.text,CONTENT)


    #阶段考评录入测试
    @parameterized.expand(test_upload_phaseExam_infos)
    def test_upload_phaseExam(self, URL, METHOD, DATA, CODE, CONTENT, expect):
        upload_phaseexam_infos = {'URL': URL, 'DATA': DATA}
        resp = student().upload_phaseexam(upload_phaseexam_infos)
        #断言
        self.assert_(resp.text, CONTENT)

    #综合成绩查询测试
    @parameterized.expand(test_query_comprehensive_infos)
    def test_query_comprehensive(self, URL, METHOD, DATA, CODE, CONTENT, expect):
        query_comprehensive_infos = {'URL': URL, 'DATA': DATA}
        resp = student().query_comprehensive(query_comprehensive_infos)
        result =resp.json()
        if result['totalRow'] == CONTENT:
            auctual = 'query_sucess'
        else:
            auctual = 'query_fail'
        self.assertEqual(auctual,expect)




if __name__ == '__main__':
    unittest.main(verbosity=2)
