import unittest
import copart_PageMap
from selenium import webdriver

class Challenge2(unittest.TestCase):

  def setUp(self):
    self.driver = webdriver.Chrome("../chromedriver.exe")

  def tearDown(self):
    self.driver.close()

  # For this challenge, look through the different ways to do assertions.
  # Then write a script that will
  #   go to copart.com,
  #   search for exotics and
  #   verify porsche is in the list of cars.
  # Use the hard assertion for this challenge.
  def test_challenge2(self):
    self.driver.get("https://copart.com")
    copart_PageMap.searchBar()



if __name__ == '__main__':
  unittest.main()