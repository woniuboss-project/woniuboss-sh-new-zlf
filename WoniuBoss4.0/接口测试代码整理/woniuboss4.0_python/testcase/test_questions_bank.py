
import unittest
from parameterized import parameterized
from util.utility import Utility

data_config_path = '../config/testdata.conf'
data_config_info = Utility.get_json(data_config_path)
query_all_data = Utility.get_excel_to_tuple(data_config_info[0])
query_dev_data = Utility.get_excel_to_tuple(data_config_info[1])

class QuestionsBankTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from common.questions_bank import QuestionsBank
        cls.questons_obj = QuestionsBank()

    @classmethod
    def tearDownClass(cls):
        pass

    # 查询所有题目接口测试
    @parameterized.expand(query_all_data)
    def test_query_question_all(self,url,method,test_data,resp_code,resp_content):
        query_all_resp = self.questons_obj.query_all(url,test_data)
        content = query_all_resp.json()
        print(content["totalRow"])
        if content["totalRow"] == 47:
            result = "querry_success"
        else:
            result = "querry_fail"
        self.assertEqual(resp_content,result)

    # 查询开发题目接口测试
    @parameterized.expand(query_dev_data)
    def test_query_question_dev(self,url,method,test_data,resp_code,resp_content):
        query_all_resp = self.questons_obj.query_all(url,test_data)
        content = query_all_resp.json()
        print(content["totalRow"])
        if content["totalRow"] == 47:
            result = "querry_success"
        else:
            result = "querry_fail"
        self.assertEqual(resp_content,result)




if __name__ == '__main__':
    unittest.main(verbosity=2)