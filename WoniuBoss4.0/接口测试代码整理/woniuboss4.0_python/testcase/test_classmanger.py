#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/26 20:21

import requests,time
import unittest
from parameterized import parameterized

from common.classmanger import classManager
from util.utility import Utility
#基本信息
test_infos=Utility.get_json('..\\config\\jtttestdata.conf')
#新增班级测试数据
test_add_class_infos=Utility.get_excel_to_tuple(test_infos[10])
#学员考勤测试数据
test_saveAttendance_infos=Utility.get_excel_to_tuple(test_infos[11])
#学员请假测试数据
test_upleave_infos=Utility.get_excel_to_tuple(test_infos[12])
#学员转班测试数据
test_transfer_class_infos=Utility.get_excel_to_tuple(test_infos[13])


class ClassManger(unittest.TestCase):

    #新增班级
    @parameterized.expand(test_add_class_infos)
    #@unittest.skip
    def test_add_class(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        add_class_infos={'URL':URL,'DATA':DATA}
        resp = classManager().add_class(add_class_infos)
        self.assertEqual(resp.text,CONTENT)

    #学员考勤
    @parameterized.expand(test_saveAttendance_infos)
    #@unittest.skip
    def test_saveAttendance(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        saveAttendance_infos={'URL':URL,'DATA':DATA}
        resp = classManager().saveAttendance(saveAttendance_infos)
        self.assertEqual(resp.text,CONTENT)

    #学员请假上传假条
    @parameterized.expand(test_upleave_infos)
    #@unittest.skip
    def test_upleave(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        upleave_infos={'URL':URL,'DATA':DATA}
        resp = classManager().upleave(upleave_infos)
        self.assertEqual(resp.text,CONTENT)



    #学员转班
    @parameterized.expand(test_transfer_class_infos)
    #@unittest.skip
    def test_transfer_class(self,URL,METHOD,DATA,CODE,CONTENT,expect):
        transfer_class_infos={'URL':URL,'DATA':DATA}
        resp = classManager().transfer_class(transfer_class_infos)
        self.assertEqual(resp.text,CONTENT)

if __name__ == '__main__':
    unittest.main(verbosity=2)