from util.service import Service


class MarketingManagement:

    def __init__(self):
        self.session = Service.get_session()

    def query_market(self,query_url,query_data):
        return  self.session.post(query_url,query_data)

    def add1(self,add_url,add_data):
        return  self.session.post(add_url,add_data)

    def add2(self,add2_url,add2_data):
        return  self.session.post(add2_url,add2_data)

    def add3(self,add3_url,add3_data):
        return  self.session.post(add3_url,add3_data)

