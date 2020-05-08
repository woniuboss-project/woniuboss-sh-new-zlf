#-*- coding:utf-8 -*-
# author JTT
# @Time:2020/4/26 20:20
from util.service import Service

class classManager:

    def __init__(self):
        self.session = Service.get_session()

    #新增班级
    def add_class(self,add_class_infos):
        return self.session.post(url=add_class_infos['URL'],data=add_class_infos['DATA'])

    #批量考勤
    def saveAttendance(self,saveAttendance_infos):
        return self.session.post(url=saveAttendance_infos['URL'],data=saveAttendance_infos['DATA'])

    #上传假条
    def upleave(self,upleave_infos):
        data=upleave_infos['DATA']
        path = data['path']
        files={'sl_stuno':(None,data['sl_stuno']),'sl_stuid':(None,data['sl_stuid']),'leave_stuid':(None,data['leave_stuid']),
               'path':(data['filename'],open(path,'rb'))}
        print(files)
        """
        files = {'sl_stuno': (None,'WNSH202004006'), 'sl_stuid': (None, '6'), 'leave_stuid': (None, '2'),
                 'path':('jiaotiao.png', open('D:\\JTT\\woniuboss\\jiaotiao.png', 'rb'))}
        resp = self.session.post(url='http://192.168.254.133:8080/WoniuBoss4.0/stuLeave/saveUpLeave',
                            files=files)
        print(resp.text)
        """
        resp = self.session.post(url=upleave_infos['URL'],files=files)
        return resp

    #学员转班
    def transfer_class(self,transfer_class_infos):
        return self.session.post(url=transfer_class_infos['URL'],data=transfer_class_infos['DATA'])

if __name__ == '__main__':
    classManager().upleave()