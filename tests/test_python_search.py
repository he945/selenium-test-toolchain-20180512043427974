import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_google(self):
        self.driver.get("http://www.google.com")
        self.assertIn("Google", self.driver.title)
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("bluemix")
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(15)
        new_elem = self.driver.find_elements_by_class_name("r");
        assert "Wikipedia" in new_elem[0].text


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

