
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class Blog_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("tutorial-env/Scripts/chromedriver.exe")

   def test_blog(self):
       user = "instructor"
       pwd = "maverick1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000/customer_list")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div[3]/table/tbody/tr/td[12]/a").click()
       time.sleep(5)
       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys("This is a test post with selenium")
       elem=driver.find_element_by_xpath('/html/body/form/button').click()
       driver.get("http://127.0.0.1:8000/customer_list")
       time.sleep(5)
       assert "edit works"

def tearDown(self):
       self.driver.close()


