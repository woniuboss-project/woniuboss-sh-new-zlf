
import unittest
from parameterized import parameterized
from util.utility import Utility

data_config_path = '../config/testdata.conf'
data_config_info = Utility.get_json(data_config_path)
query_market_data = Utility.get_excel_to_tuple(data_config_info[12])
print(query_market_data)
add1_data = Utility.get_excel_to_tuple(data_config_info[13])
add2_data = Utility.get_excel_to_tuple(data_config_info[14])
add3_data = Utility.get_excel_to_tuple(data_config_info[15])
class QuestionsBankTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from common.marketing_management import MarketingManagement
        cls.market_obj = MarketingManagement()

    @classmethod
    def tearDownClass(cls):
        pass

    # 查询所有题目接口测试
    @parameterized.expand(query_market_data)
    def test_query_market(self,url,method,test_data,resp_code,resp_content):
        query_market_resp = self.market_obj.query_market(url,test_data)
        content = query_market_resp.json()
        print(content["totalRow"])
        if content["totalRow"] == 61:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content,result)

    @parameterized.expand(add1_data)
    def test_add1(self, url, method, test_data, resp_code, resp_content):
        add1_resp = self.market_obj.add1(url, test_data)
        content = add1_resp.json()
        print(content["totalRow"])
        if content["totalRow"] == 1:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content, result)

    @parameterized.expand(add2_data)
    def test_add2(self, url, method, test_data, resp_code, resp_content):
        add2_resp = self.market_obj.add2(url, test_data)
        content = add2_resp.json()
        print(content["totalRow"])
        if content["totalRow"] == 12:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content, result)

    @parameterized.expand(add3_data)
    def test_add3(self, url, method, test_data, resp_code, resp_content):
        add3_resp = self.market_obj.add3(url, test_data)
        content = add3_resp.json()
        print(content["totalRow"])
        if content["totalRow"] == 3:
            result = "query ok"
        else:
            result = "query fail"
        self.assertEqual(resp_content, result)




if __name__ == '__main__':
    unittest.main(verbosity=2)