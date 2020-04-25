
import unittest
from parameterized import parameterized

from common.employee_manage import EmployeeManage
from util.utility import Utility

data_config_path = '../config/fei_testdata.conf'
data_config_info = Utility.get_json(data_config_path)


add_info = Utility.get_excel_to_tuple(data_config_info[3])
modify_info = Utility.get_excel_to_tuple(data_config_info[4])
query_info = Utility.get_excel_to_tuple(data_config_info[5])
class AdminManageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = EmployeeManage()

    @parameterized.expand(add_info)
    def test_add(self,url,method,test_data,resp_code,resp_content):
        resp = self.obj.add(url,test_data)
        print(resp.text)
        self.assertEqual(resp_content,resp.text)

    @parameterized.expand(modify_info)
    def test_modify(self, url, method, test_data, resp_code, resp_content):
        resp = self.obj.modify(url, test_data)
        self.assertEqual(resp_content, resp.text)

    @parameterized.expand(query_info)
    def test_query(self, url, method, test_data, resp_code, resp_content):
        resp = self.obj.query(url, test_data)
        if resp.json()['totalRow'] == 3:
            result = 'query_success'
        self.assertEqual(resp_content, result)
if __name__ == '__main__':
    unittest.main(verbosity=2)