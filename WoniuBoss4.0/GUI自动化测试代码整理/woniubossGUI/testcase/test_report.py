
from parameterized import parameterized
import unittest
import time

# 获取测试数据
from common.report import Report
from util.service import Service
from util.utility import Utility

date_datas = Utility.get_json('../config/lf_testdata.conf')
console_data = Utility.get_excel_to_tuple(date_datas[0])
sale_data = Utility.get_excel_to_tuple(date_datas[1])
market_data = Utility.get_excel_to_tuple(date_datas[2])
job_data = Utility.get_excel_to_tuple(date_datas[3])

path = '..\\config\\base.conf'
class TestReport(unittest.TestCase):

    def setUp(self):
        print('test start')
        self.driver = Service.get_driver(path)
        Service.miss_login(self.driver, path)
        self.driver.find_element_by_link_text(u'报表中心').click()
        self.report = Report(self.driver)

    def tearDown(self):
        print('test over')
        time.sleep(2)
        self.driver.quit()

    # 咨询部
    @parameterized.expand(console_data)
    def test_console_query_one(self, starttime, endtime, expect):
        self.report.click_console()
        # 搜索
        self.report.input_console_date(starttime, endtime)
        self.report.click_cnsole_query()
        sql_one = 'select count(last_status) from customer where work_id = "23" and last_status="新认领"'
        result_one = Utility.query_one(path, sql_one)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[8]').text == result_one[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)


    # 电销部
    @parameterized.expand(sale_data)
    def test_sale_data_one(self, starttime, endtime, expect):
        self.report.click_sale()
        # 搜索
        self.report.input_sale_date(starttime, endtime)
        self.report.click_sale_query()
        sql_one = 'select count(last_status) from customer where work_id = "66" and last_status="已认领"'
        result_one = Utility.query_one(path, sql_one)
        if self.driver.find_element_by_xpath('//table[@id="成都"]/tbody/tr[2]/td[9]').text == result_one[0]:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)


    # 市场部
    @parameterized.expand(market_data)
    def test_market_data_one(self, starttime, endtime, expect):
        self.report.click_market()
        # 搜索
        self.report.input_market_date(starttime, endtime)
        self.report.click_market()
        sql_one = 'select count(department_id) from customer where create_time="2020-04-13"  '
        result_one = Utility.query_one('../config/base.conf', sql_one)
        if result_one[0] == 2:
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)


    # 就业部
    @parameterized.expand(job_data)
    def test_job_data_one(self, starttime, endtime, expect):
        self.report.click_job()
        # 搜索
        self.report.input_job_date(starttime, endtime)
        self.report.click_job_cnsole_query()
        if self.driver.find_element_by_xpath('//table[@id="jobTb"]/tbody/tr/td[1]').text == '甘立文':
            actual = 'query-pass'
        else:
            actual = 'query-fail'
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    unittest.main(verbosity=2)
