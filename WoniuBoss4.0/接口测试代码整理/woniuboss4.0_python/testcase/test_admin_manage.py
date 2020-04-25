
import unittest
from parameterized import parameterized

from common.admin_manage import AdminManage
from util.utility import Utility

data_config_path = '../config/fei_testdata.conf'
data_config_info = Utility.get_json(data_config_path)

test_info = Utility.get_excel_to_tuple(data_config_info[6])
print('test_info',test_info)
class ReportCenterQueryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = AdminManage()

    @parameterized.expand(test_info)
    def test_admin_manage(self, url, method, test_data, resp_code, resp_content):
        resp = self.obj.admin_manage(url, test_data)

        print('============',resp.text)
        if resp_content != 'query_success':
            result = resp.text
        else:
            if resp.json()['pageNumber'] != None:
                result = 'query_success'
        self.assertEqual(resp_content, result)



if __name__ == '__main__':
    unittest.main(verbosity=2)