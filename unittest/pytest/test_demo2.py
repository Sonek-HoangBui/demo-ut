# from asyncio import subprocess
# import asyncio
# from cmath import log
# from nis import cat
# import os
# from pickle import TRUE
# import time
import unittest
import requests
import responses
import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# import json
# from AppKit import NSPasteboard, NSStringPboardType


# def getElement(driver, xpath):
#     try:
#         return driver.find_element(by=By.XPATH,value=xpath)
#     except:
#         return None

# def handleClick(driver, xpath):
#     try:
#         driver.find_element(by=By.XPATH,value=xpath).click()
#     except:
#         return None

class GameGuild(unittest.TestCase):
    domain = "https://dev.nft.mobilelab.vn"
    # domainCollection = "https://dev.nft.mobilelab.vn/collection/383"
    domainCollection = "https://dev.nft.mobilelab.vn/collection/554"
    def setUpModule(self):
        print('setUpModule')
    def tearDownModule(self):
        print('setUpModule')
    def setUp(self):
        print('setUp')
        # with open('session.txt') as f:
        #     session = f.read()
        #     script_session = "window.localStorage.setItem('session',`{0}`);".format(session)
        #     self.driver.execute_script(script_session)
        # self.driver.refresh()

    def setUpClass():
        print('setUpClass')

    def tearDown(self):
        print('tearDown')

    def tearDownClass():
        print('tearDownClass')

    @responses.activate  
    def test_false(self):
        responses.add(**{
            'method'         : responses.GET,
            'url'            : 'http://example.com/api/123',
            'body'           : '{"error": "reason"}',
            'status'         : 404,
            'content_type'   : 'application/json',
            'adding_headers' : {'X-Foo': 'Bar'}
        })
        response = requests.get("http://example.com/api/123")
        print(response.json(), ": ???")
        self.assertEqual({'error': 'reason'}, response.json())
        self.assertEqual(404, response.status_code)
    def test_true(self):
        print('=== assert test true ===')
        self.assertEqual(1, 1)

    def test_with_local_fixture(local_fixture):
        """
        Fixtures can be invoked simply by having a positional arg
        with the same name as a fixture:
        """
        print("Running test_with_local_fixture...")
        assert True

    def test_zero_division(self):
        with pytest.raises(FileExistsError):
            1/0

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            1/0

    @pytest.fixture
    def local_fixture():
        """
        Fixtures are callables decorated with @fixture
        """
        print("\n(Doing Local Fixture setup stuff!)")


    def test_with_global_fixture(global_fixture):
        """
        Fixtures can also be shared across test files (see conftest.py)
        """
        print("Running test_with_global_fixture...")
    # def run():
    #     print('run')
    
    # def skipTest():
    #     print('skipTest')

    # # def shortDescription():
    # #     return 'Test staking'

    # def debug():
    #     return 'debug'

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


print(__name__)