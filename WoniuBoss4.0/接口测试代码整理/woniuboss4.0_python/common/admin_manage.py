from util.service import Service


class AdminManage:

    def __init__(self):
        self.session = Service.get_session()

    def admin_manage(self,url,data):
        return  self.session.post(url,data)

