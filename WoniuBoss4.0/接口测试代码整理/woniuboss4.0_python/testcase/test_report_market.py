
import unittest
from parameterized import parameterized

from common.report_market import ReportMarketBank
from util.utility import Utility

data_config_path = '../config/fei_testdata.conf'
data_config_info = Utility.get_json(data_config_path)

query_all_data = Utility.get_excel_to_tuple(data_config_info[0])

class ReportMarkTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.obj = ReportMarketBank()

    @parameterized.expand(query_all_data)
    def test_query_question_all(self,url,method,test_data,resp_code,resp_content):
        resp = self.obj.query_all(url,test_data)
        content = resp.json()
        print(content[len(content)-1]["num"])
        if content[len(content)-1]["num"] == 2:
            result = "querry_success"
        else:
            result = "querry_fail"
        self.assertEqual(resp_content,result)

if __name__ == '__main__':
    unittest.main(verbosity=2)