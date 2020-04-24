# -*- coding: utf-8 -*-#

import requests

from util.utility import Utility

class Service:

	@classmethod
	def get_session(cls):
		base_info = Utility.get_json('../config/base.conf')
		login_url = "%s://%s:%s/%s" %(base_info['PROTOCOL'],base_info['HOSTNAME'],base_info['PORT'],base_info['AURL'])
		login_data = {"userName":base_info["USERNAME"],"userPass":base_info["PASSWORD"],"checkcode":base_info["VERIFYCODE"],"remember":base_info["REMEMBER"]}
		session = requests.session()
		session.post(login_url,login_data)
		return session
