import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Challenge3(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome("../chromedriver.exe")

  def tearDown(self):
    self.driver.close()

  # For this challenge,
  # go to copart and
  # print a list of all the “Popular Items”
  #   of vehicle
  #   Make / Models
  #   URL and href for each type
  # on the home page
  # This list can dynamically change depending on what is authored by the content creator but using a loop will
  # make sure that everything will be displayed regardless of the list size.
  def test_challenge_3(self):
    self.driver.get("https://copart.com")
    popularMake = self.driver.find_elements(By.CSS_SELECTOR, "[href*='/popular/make']")
    popularModel = self.driver.find_elements(By.CSS_SELECTOR, "[href*='/popular/model']")
    makeModel = popularMake + popularModel
    for popular in makeModel:
      print(popular.text + '--' + popular.get_attribute('href'))

if __name__ == '__main__':
  unittest.main()