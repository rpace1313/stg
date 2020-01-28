import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
    porcheTrue = False
    self.driver.get("https://copart.com")
    search = self.searchBar()
    search.send_keys('exotics')
    search.send_keys(Keys.ENTER)
    sleep(4)
    makes = self.driver.find_element_by_id('serverSideDataTable')
    for tr in makes.find_elements_by_tag_name('td'):
      for span in tr.find_elements_by_tag_name('span'):
        if span.text == 'PORSCHE':
          porcheTrue = True
          break
        else:
          continue
    assert porcheTrue

  def searchBar(self):
    return self.driver.find_element_by_id('input-search')

if __name__ == '__main__':
  unittest.main()