import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class IDVsXpath(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument('--headless')
        self.driver = webdriver.Chrome('Chromedriver.exe', options=option)
        self.driver.get('http://duckduckgo.com/')

    def test_comparations(self):
        total_time = 0.0
        for i in range(1000):
            start_time = time.time()
            a = self.driver.find_element_by_id('search_form_input_homepage')
            #b = self.driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
            end_time = time.time()
            total_time = total_time + end_time - start_time
            print(end_time - start_time)
        print('TOTAL TIME')
        print(total_time/1000)
        print('TIME TOTAL OF THE TEST')
        print(total_time)
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
