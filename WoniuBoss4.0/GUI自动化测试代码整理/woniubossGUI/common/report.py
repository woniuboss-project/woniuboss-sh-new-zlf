import time

from util.service import Service


class Report:

    def __init__(self, driver):
        self.driver = driver


    # 咨询部
    def click_console(self):
        self.driver.find_element_by_link_text('咨询部').click()

    def input_console_date(self, starttime, endtime):
        c_starttime = self.driver.find_element_by_name('s_consulttime')
        Service.send_input(c_starttime, starttime)
        time.sleep(2)
        c_endtime = self.driver.find_element_by_name('e_consulttime')
        Service.send_input(c_endtime, endtime)

    def click_cnsole_query(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[1]').click()

    def click_evedate_console(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[2]').click()

    def click_eveday_console(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[3]').click()

    def click_eveweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[4]').click()

    def click_evemonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[5]').click()

    def click_oldweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[6]').click()

    def click_oldmonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[7]').click()

    def click_eveyear_console(self):
        self.driver.find_element_by_xpath('//div[@id="consulting-1"]/div[1]/div[1]/button[8]').click()

    # 电销部
    def click_sale(self):
        self.driver.find_element_by_link_text('电销部').click()

    def input_sale_date(self, starttime, endtime):
        c_starttime = self.driver.find_element_by_name('s_consulttime')
        Service.send_input(c_starttime, starttime)
        time.sleep(2)
        c_endtime = self.driver.find_element_by_name('e_consulttime')
        Service.send_input(c_endtime, endtime)

    def click_sale_query(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[1]').click()

    def click_sale_evedate_console(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[2]').click()

    def click_sale_eveday_console(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[3]').click()

    def click_sale_veweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[4]').click()

    def click_sale_evemonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[5]').click()

    def click_sale_oldweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[6]').click()

    def click_sale_oldmonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[7]').click()

    def click_sale_eveyear_console(self):
        self.driver.find_element_by_xpath('//div[@id="electric"]/div[1]/div[1]/div[1]/button[8]').click()

    # 市场部
    def click_market(self):
        self.driver.find_element_by_link_text('市场部').click()

    def input_market_date(self, starttime, endtime):
        c_starttime = self.driver.find_element_by_name('s_sourcetime')
        Service.send_input(c_starttime, starttime)
        time.sleep(2)
        c_endtime = self.driver.find_element_by_name('e_sourcetime')
        Service.send_input(c_endtime, endtime)

    def click_market_cnsole_query(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[1]').click()

    def click_market_evedate_console(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[2]').click()

    def click_market_eveday_console(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[3]').click()

    def click_market_eveweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[4]').click()

    def click_market_evemonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[5]').click()

    def click_market_oldweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[6]').click()

    def click_market_oldmonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[7]').click()

    def click_market_eveyear_console(self):
        self.driver.find_element_by_xpath('//div[@id="market"]/div[1]/div[1]/button[8]').click()

    # 就业部
    def click_job(self):
        self.driver.find_element_by_link_text('就业部').click()

    def input_job_date(self, starttime, endtime):
        c_starttime = self.driver.find_element_by_name('s_jobtime')
        Service.send_input(c_starttime, starttime)
        time.sleep(2)
        c_endtime = self.driver.find_element_by_name('e_jobtime')
        Service.send_input(c_endtime, endtime)

    def click_job_cnsole_query(self):
        self.driver.find_element_by_xpath('//div[@id="job"]/div[1]/div[1]/button[1]').click()

    def click_job_eveday_console(self):
        self.driver.find_element_by_xpath('//div[@id="job"]/div[1]/div[1]/button[2]').click()

    def click_job_eveweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="job"]/div[1]/div[1]/button[3]').click()

    def click_job_evemonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="job"]/div[1]/div[1]/button[4]').click()

    def click_job_oldweek_console(self):
        self.driver.find_element_by_xpath('//div[@id="job"]/div[1]/div[1]/button[5]').click()

    def click_job_oldmonth_console(self):
        self.driver.find_element_by_xpath('//div[@id="job"]/div[1]/div[1]/button[6]').click()

    def click_job_eveyear_console(self):
        self.driver.find_element_by_xpath('//div[@id="job"]/div[1]/div[1]/button[7]').click()
