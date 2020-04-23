# -*- coding: utf-8 -*-#

import requests

# from util.utility import Utility


class Service:

	@classmethod
	def get_session(cls):
		# base_info = Utility.get_json('../config/base.conf')
		# login_url = "%s://%s:%s/%s/" %(base_info['PROTOCOL'],base_info['HOSTNAME'],base_info['PORT'],base_info['AURL'])
		# login_data = {"username":base_info["USERNAME"],"password":base_info["PASSWORD"],"verifycode":base_info["VERIFYCODE"]}
		login_url= r'http://192.168.52.130:8080/WoniuSales-20180508-V1.4-bin/user/login'
		login_data = {"username":"admin","password":"milor123","verifycode":"0000"}
		session = requests.session()
		resp =session.post(login_url,login_data)
		session_id = resp.cookies
		print(session_id)

if __name__ == '__main__':
	Service.get_session()