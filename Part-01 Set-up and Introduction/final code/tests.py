from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

Example 1

class Hosttest(LiveServerTestCase):
  	
	def testhomepage(self):
		driver = webdriver.Chrome()

		driver.get('http://127.0.0.1:8000/')
		
		assert "Hello, world!" in driver.title

Example 2

class LoginFormTest(LiveServerTestCase):

	def testform(self):
		driver = webdriver.Chrome()

		driver.get('http://127.0.0.1:8000/accounts/login/')

		time.sleep(3)

		user_name = driver.find_element_by_name('username')
		user_password = driver.find_element_by_name('password')

		time.sleep(3)

		submit = driver.find_element_by_id('submit')

		user_name.send_keys('admin')
		user_password.send_keys('admin')

		submit.send_keys(Keys.RETURN)

		assert 'admin' in driver.page_source