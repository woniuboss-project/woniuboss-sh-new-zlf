from util.service import Service


class QuestionsBank:

    def __init__(self):
        self.session = Service.get_session()

    # 查询所有题型
    def query_all(self,query_url,query_all_data):
        return  self.session.post(query_url,query_all_data)

    # 查询开发的题型
    def query_dev_questions(self,query_url,query_dev_data):
        return  self.session.post(query_url,query_dev_data)

    # 添加单选题
    def add_choice_question(self,add_url,add_data):
        return self.session.post(add_url,add_data)

    # 添加填空题
    def add_blank_question(self, add_url, add_data):
        return self.session.post(add_url, add_data)

    # 添加简答题
    def add_answer_question(self,add_url,add_data):
        return self.session.post(add_url,add_data)

    # 自动出题
    def create_test(self,create_url,create_data):
        return self.session.post(create_url, create_data)

    # 替换题目
    def replace_test(self,replace_url,replace_data):
        return self.session.post(replace_url,replace_data)

    # 下载文件
    def download_file(self,file_url):
        return self.session.get(file_url)