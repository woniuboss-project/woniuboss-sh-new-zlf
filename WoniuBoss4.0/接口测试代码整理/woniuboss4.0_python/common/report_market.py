from util.service import Service


class ReportMarketBank:

    def __init__(self):
        self.session = Service.get_session()

    def query_all(self,url,data):
        return  self.session.post(url,data)

