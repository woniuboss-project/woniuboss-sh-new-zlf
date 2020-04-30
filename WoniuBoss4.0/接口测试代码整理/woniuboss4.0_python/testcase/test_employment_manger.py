import unittest

from parameterized import parameterized

from util.utility import Utility

data_config_path = '../config/testdata.conf'
data_config_info = Utility.get_json(data_config_path)
query_all_data = Utility.get_excel_to_tuple(data_config_info[8])
query_data_by_result = Utility.get_excel_to_tuple(data_config_info[9])
add_data = Utility.get_excel_to_tuple(data_config_info[10])
query_interview_data = Utility.get_excel_to_tuple(data_config_info[11])
query_entry_data = Utility.get_excel_to_tuple(data_config_info[12])
save_entry_data = Utility.get_excel_to_tuple(data_config_info[13])
query_business_data = Utility.get_excel_to_tuple(data_config_info[14])
modify_business_data = Utility.get_excel_to_tuple(data_config_info[15])



class EmploymentMangerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from common.employmentmanger import EmploymentManger
        cls.emp_obj = EmploymentManger()

    @classmethod
    def tearDownClass(cls):
        pass


    # 查询所有学生信息接口测试
    @parameterized.expand(query_all_data)
    def test_query_student(self,url,method,test_data,resp_code,resp_content):
        query_resp = self.emp_obj.query_student(url,test_data)
        if query_resp.json()["totalRow"] == 8:
            result = "query_success"
        else:
            result = "query_fail"
        self.assertEqual(resp_content,result)

    # 根据技术面试结果查询学生信息接口测试
    @parameterized.expand(query_data_by_result)
    def test_query_student_by_result(self,url,method,test_data,resp_code,resp_content):
        query_resp = self.emp_obj.query_student(url,test_data)
        if query_resp.text == "success":
            result = "query_success"
        else:
            result = "query_fail"
        self.assertEqual(resp_content, result)

    # 新增学员面试记录接口测试
    @parameterized.expand(add_data)
    def test_add_interview(self,url,method,test_data,resp_code,resp_content):
        self.emp_obj.add_interview(url)

    # 查询学员面试记录接口测试
    @parameterized.expand(query_interview_data)
    def test_query_interview(self,url,method,test_data,resp_code,resp_content):
        query_resp = self.emp_obj.query_interview_record(url, test_data)
        if query_resp.json()["totalRow"] == 3:
            result = "query_success"
        else:
            result = "query_fail"
        self.assertEqual(resp_content,result)

    # 查询学员入职信息接口测试
    @parameterized.expand(query_entry_data)
    def test_query_entry_info(self,url,method,test_data,resp_code,resp_content):
        query_resp = self.emp_obj.query_entry_info(url,test_data)
        if query_resp.json()["totalRow"] == 8:
            result = "query_success"
        else:
            result = "query_fail"
        self.assertEqual(resp_content,result)

    # 保存学员入职信息接口测试
    @parameterized.expand(save_entry_data)
    def test_save_entry_info(self,url,method,test_data,resp_code,resp_content):
        save_resp = self.emp_obj.save_entry_info(url,test_data)
        result = save_resp.text
        self.assertEqual(result,resp_content)

    # 查询企业客户接口测试
    @parameterized.expand(query_business_data)
    def test_query_business(self,url,method,test_data,resp_code,resp_content):
        query_resp = self.emp_obj.query_business(url,test_data)
        if query_resp.json()["totalRow"] == 3:
            result = "query_success"
        else:
            result = "query_fail"
        self.assertEqual(resp_content,result)

    # 修改企业客户信息接口测试
    @parameterized.expand(modify_business_data)
    def test_modify_business(self,url,method,test_data,resp_code,resp_content):
        modify_resp = self.emp_obj.modify_business_info(url)
        result = modify_resp.text
        self.assertEqual(resp_content,result)





if __name__ == '__main__':
    unittest.main(verbosity=2)

