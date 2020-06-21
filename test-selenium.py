import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://www.python.org"

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:\\Users\\rac\\Documents\\workspace\\geckodriver-v0.26.0-win64\\geckodriver.exe')

    def tearDown(self):
        self.driver.close()
        
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get(URL)
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
    
    def test_search_in_python_org_success(self):
        driver = self.driver
        driver.get(URL)
        input_id_search_field = driver.find_element_by_id("id-search-field")
        button_id_submit = driver.find_element_by_id("submit")
        input_id_search_field.send_keys("string")
        button_id_submit.click()
        assert "Python Patterns - An Optimization Anecdote" in driver.page_source

if __name__ == "__main__":
    unittest.main()
