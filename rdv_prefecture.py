# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
	def setUp(self):
		# AppDynamics will automatically override this web driver
		# as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
		self.driver = webdriver.Chrome('chromedriver.exe')
		self.driver.implicitly_wait(30)
		self.base_url = "http://www.val-de-marne.gouv.fr/booking/create/4963/1"
		self.verificationErrors = []
		self.accept_next_alert = True
    
	def test_app_dynamics_job(self):
		driver = self.driver
		driver.get("http://www.val-de-marne.gouv.fr/booking/create/4963/1")
		driver.find_element_by_id("planning5955").click()
		driver.find_element_by_id("submit_Booking").click()
		# driver.find_element_by_xpath("//input[@id='planning5968']").click()
		# driver.implicitly_wait(30)
		# driver.find_element_by_class_name("Bbutton").click()
		# driver.implicitly_wait(30)
		# driver.get("http://www.val-de-marne.gouv.fr/booking/create/4963/1")
		# driver.implicitly_wait(30)
		# driver.find_element_by_xpath("//input[@id='planning5973']").click()
		# driver.implicitly_wait(30)
		# driver.find_element_by_class_name("Bbutton").click()

	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException as e: return False
		return True
    
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException as e: return False
		return True
    
	def close_alert_and_get_its_text(self):
		try:
			alert = self.driver.switch_to_alert()
			alert_text = alert.text
			if self.accept_next_alert:
				alert.accept()
			else:
				alert.dismiss()
			return alert_text
		finally: self.accept_next_alert = True

	def tearDown(self):
		# To know more about the difference between verify and assert,
		# visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
		self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
	unittest.main()
