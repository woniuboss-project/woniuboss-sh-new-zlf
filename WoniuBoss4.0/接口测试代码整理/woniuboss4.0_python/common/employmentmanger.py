
from util.service import Service


class EmploymentManger:

    def __init__(self):
        self.session = Service.get_session()

    # 查询学生的信息
    def query_student(self,query_url,query_data):
        return self.session.post(query_url,query_data)

    # 新增学生面试记录
    def add_interview(self,add_url):
        return self.session.get(add_url)

    # 查询学生面试记录
    def query_interview_record(self,query_url,query_data):
        return self.session.post(query_url,query_data)

    # 查询学员入职信息
    def query_entry_info(self,query_url,query_data):
        return self.session.post(query_url,query_data)

    # 新增入职学员的入职信息
    def save_entry_info(self,add_url,add_data):
        return self.session.post(add_url,add_data)

    # 查询企业客户信息
    def query_business(self,query_url,query_data):
        return self.session.post(query_url,query_data)

    # 修改企业客户信息
    def modify_business_info(self,modify_url):
        return self.session.get(modify_url)
