#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/24 14:29

from util.service import Service

import requests
class student:

    def __init__(self):
        self.session = Service.get_session()


    #学员信息查询
    def query_student(self,query_infos):
        resp = self.session.post(url=query_infos['URL'],data=query_infos['DATA'])
        return resp

    #晨考和作业
    def Mornexam_homework(self,testinfos):
        return self.session.post(url=testinfos['URL'],data=testinfos['DATA'])

    #周考成绩上传
    def upload_weekexam(self,upload_weekexam_infos):
        filename=upload_weekexam_infos['DATA']['filename']
        path ='C:\\Users\\EDZ\\Desktop\\{}'.format(filename)
        #upload_file = {'filename': ('weekexam.xls', open('C:\\Users\\EDZ\\Desktop\\weekexam.xls', 'rb'))}
        upload_file={'filename':(filename,open(path,'rb'))}
        resp=self.session.post(url=upload_weekexam_infos['URL'],files=upload_file)
        return resp

    # 阶段成绩上传
    def upload_phaseexam(self, upload_phaseexam_infos):
        filename = upload_phaseexam_infos['DATA']['filename']
        path = 'C:\\Users\\EDZ\\Desktop\\{}'.format(filename)
        upload_file = {'filename': (filename, open(path, 'rb'))}
        resp = self.session.post(url=upload_phaseexam_infos['URL'], files=upload_file)
        return resp

    #综合成绩查询
    def query_comprehensive(self, query_comprehensive_infos):
        resp = self.session.post(url=query_comprehensive_infos['URL'],data=query_comprehensive_infos['DATA'])
        return resp

    #学员信息修改
    def edit_student(self,edit_infos):
        """
        files = {'stu.student_id': (None, '8'), 'stu.student_name': (None, '王二'), 'stu.student_no': (None, 'WNSH202004008'),
                 'class_no':(None, 'WNSHC099'),'stu.tel':(None, '0'),'stu.sex':(None, '女'),'stu.status':(None, '02'),'stu.need_fee':(None, '01'),
                 'stu.QQ': (None, ''),'stu.source': (None, '04'),'stu.emergency_person': (None, ''),'stu.emergency_tel': (None, ''),'stu.school': (None, ''),
                 'stu.education': (None, '03'),'stu.major': (None, ''),'stu.IDnumber': (None, ''),'stu.graduation_time': (None, ''),'stu.age': (None, '')
                 }
        """
        resp = self.session.post(url=edit_infos['URL'],files=edit_infos['files'])

        print(resp.text)
        return resp

    def download_file_method(self):

        # 下面是下载文件的方法，对于下载的文件保存时注意文字编码
        resp = self.session.get('http://192.168.254.133:8080/WoniuBoss4.0/static/js/bootstrap-table.css')
        with open('C:\\Users\\EDZ\\Desktop\\a.xls', 'wb') as f:
            f.write(resp.content)


if __name__ == '__main__':
    student().download_file_method()