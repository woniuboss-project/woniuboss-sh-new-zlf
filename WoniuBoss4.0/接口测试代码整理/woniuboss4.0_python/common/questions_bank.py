from util.service import Service


class QuestionsBank:

    def __init__(self):
        self.session = Service.get_session()

    def query_all(self,query_url,query_all_data):
        return  self.session.post(query_url,query_all_data)

    def query_dev_questions(self,query_url,query_dev_data):
        return  self.session.post(query_url,query_dev_data)