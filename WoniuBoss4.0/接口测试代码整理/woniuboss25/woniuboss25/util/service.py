# -*- coding: utf-8 -*-#

import requests

from util.utility import Utility


class Service:

	@classmethod
	def get_session(cls):
		base_info = Utility.get_json('..\\config\\base.conf')
		#login_url = "%s://%s:%s/%s/" %(base_info['PROTOCOL'],base_info['HOSTNAME'],base_info['PORT'],base_info['AURL'])
		login_url ='http://192.168.254.133:8080/WoniuBoss4.0/login/userLogin'
		login_data = {"userName":base_info["USERNAME"],"userPass":base_info["PASSWORD"],"checkcode":base_info["VERIFYCODE"]}
		session = requests.session()
		session.post(url=login_url,data=login_data)
		return session
		#session_id = resp.cookies
		#return session_id

if __name__ == '__main__':
	Service.get_session()