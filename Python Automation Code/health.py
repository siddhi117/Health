import unittest
from selenium import webdriver
import time

class Health(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_submission(self):
        driver = self.driver

        driver.get('https://hidden-chamber-33381.herokuapp.com/#/')
        driver.maximize_window()                                                                      #Maximize the window
        assert 'health' in driver.title
        time.sleep(5)

        signin = driver.find_element_by_xpath(' //a[@class = \'alert-link\'] ')                       #Sign in Link
        signin.click()
        time.sleep(3)

        user_name  = driver.find_element_by_id('username')                                            #Username
        user_name.send_keys("admin")
        time.sleep(2)

        password = driver.find_element_by_id('password')                                              #Password
        password.send_keys("admin")                            
        time.sleep(2)

        submit = driver.find_element_by_xpath(' //button[@class= \'btn btn-primary\'] ')              #Submit
        submit.click()
        time.sleep(10)


    def teardown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()


