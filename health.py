import unittest
from selenium import webdriver
import time

class Health(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_submission(self):
        driver = self.driver

        driver.get('https://hidden-chamber-33381.herokuapp.com/#/')
        driver.maximize_window()
        assert 'health' in driver.title
        time.sleep(5)

        #signin = driver.find_element_by_class_name('alert-link')
        signin = driver.find_element_by_xpath(' //a[@class = \'alert-link\'] ')
        signin.click()
        time.sleep(3)

        user_name  = driver.find_element_by_id('username')
        user_name.send_keys("admin")

        password = driver.find_element_by_id('password')
        password.send_keys("admin")

        submit = driver.find_element_by_xpath(' //button[@class= \'btn btn-primary\'] ')
        submit.click()
        time.sleep(10)


    def teardown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


