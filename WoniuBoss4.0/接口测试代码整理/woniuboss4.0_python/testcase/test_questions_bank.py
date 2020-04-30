
import unittest
from parameterized import parameterized
from util.utility import Utility

data_config_path = '../config/testdata.conf'
data_config_info = Utility.get_json(data_config_path)
query_all_data = Utility.get_excel_to_tuple(data_config_info[0])
query_dev_data = Utility.get_excel_to_tuple(data_config_info[1])
add_choice_data = Utility.get_excel_data_to_tuple(data_config_info[2])
add_blank_data = Utility.get_excel_data_to_tuple(data_config_info[3])
add_answer_data = Utility.get_excel_data_to_tuple(data_config_info[4])
create_test_data = Utility.get_excel_to_tuple(data_config_info[5])
replace_test_data = Utility.get_excel_data_to_tuple(data_config_info[6])
download_test_data = Utility.get_excel_to_tuple(data_config_info[7])

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
        if content["totalRow"] == 69:
            result = "query_success"
        else:
            result = "query_fail"
        self.assertEqual(resp_content,result)

    # 查询开发题目接口测试
    @parameterized.expand(query_dev_data)
    def test_query_question_dev(self,url,method,test_data,resp_code,resp_content):
        query_all_resp = self.questons_obj.query_dev_questions(url,test_data)
        content = query_all_resp.json()
        result = None
        for i in range(len(content["list"])):
            if content["list"][i]["orientation"] != "开发":
                result = "query_fail"
                break
            else:
                result = "query_success"
        self.assertEqual(resp_content,result)

    # 新增单选题接口测试
    @parameterized.expand(add_choice_data)
    def test_add_choice_question(self,url,method,test_data,resp_code,resp_content):
        import json
        user_dict = json.loads(test_data)
        add_choice_resp = self.questons_obj.add_choice_question(url,user_dict)
        result = add_choice_resp.text
        self.assertEqual(resp_content, result)

    # 新增填空题接口测试
    @parameterized.expand(add_blank_data)
    def test_add_blank_question(self,url,method,test_data,resp_code,resp_content):
        import json
        user_dict = json.loads(test_data)
        add_bland_resp = self.questons_obj.add_blank_question(url, user_dict)
        result = add_bland_resp.text
        self.assertEqual(resp_content, result)

    # 新增解答题接口测试
    @parameterized.expand(add_answer_data)
    def test_add_answer_question(self,url,method,test_data,resp_code,resp_content):
        import json
        user_dict = json.loads(test_data)
        add_answer_resp = self.questons_obj.add_answer_question(url, user_dict)
        result = add_answer_resp.text
        self.assertEqual(resp_content, result)

    # 自动出题接口测试
    @parameterized.expand(create_test_data)
    def test_create_tests(self,url,method,test_data,resp_code,resp_content):
        create_test_resp = self.questons_obj.create_test(url, test_data)
        if "自动出题" in create_test_resp.text:
            result = "create_success"
        else:
            result = "create_fail"
        self.assertEqual(resp_content,result)

    # 自动替换题目接口测试
    @parameterized.expand(replace_test_data)
    def test_replace_tests(self,url,method,test_data,resp_code,resp_content):
        replace_test_resp =  self.questons_obj.replace_test(url,test_data)
        if resp_code == replace_test_resp.status_code:
            result = "replace_success"
        else:
            result = "replace_fail"

    # 下载试题接口测试
    @parameterized.expand(download_test_data)
    def test_download_file(self,url,method,test_data,resp_code,resp_content):
        self.questons_obj.download_file(url)









if __name__ == '__main__':
    unittest.main(verbosity=2)