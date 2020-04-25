from util.service import Service


class EmployeeManage:

    def __init__(self):
        self.session = Service.get_session()

    def add(self,url,data):
        return  self.session.post(url,data)

    def modify(self,url,data):
        return  self.session.post(url,data)

    def query(self,url,data):
        return  self.session.post(url,data)