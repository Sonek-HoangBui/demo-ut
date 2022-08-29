from nis import cat
from pickle import TRUE
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
import csv
from selenium.webdriver.common.keys import Keys

def getElement(driver, xpath):
    try:
        return driver.find_element(by=By.XPATH,value=xpath)
    except:
        return None

def handleClick(driver, xpath):
    try:
        driver.find_element(by=By.XPATH,value=xpath).click()
    except:
        pass

class SimpleTest(unittest.TestCase):
    domain = "https://dev.api.crypto.mobilelab.vn/staking"
    showStakeInfoBtnEl = "(//button[@type='button'])[2]"
    searchInputEl = "//input[@type='text']"
    emptyImgEl = "//div[@class='ant-empty-image']"
    clearEl = "//span[@aria-label='close-circle']"
    packageEl = "//td[@class='ant-table-cell']//span[@class='pl-small']"
    keySearch = "USDT"
    

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.domain)

        with open('session.txt') as f:
            session = f.read()
            script_session = "window.localStorage.setItem('session',`{0}`);".format(session)
            self.driver.execute_script(script_session)
        self.driver.refresh()
        self.driver.get(self.domain)

    def handleSearchTxT(self, element, keySearch):
        print('handleSearchTxT')
        element.send_keys(keySearch)

        time.sleep(2)
        emptyEl = getElement(self.driver, self.emptyImgEl)
        # self.assertEqual(emptyEl.is_displayed(), True, "Failed size is not empty")

        if emptyEl is None:
            packagesEl = self.driver.find_elements(by=By.XPATH, value=self.packageEl)
            print(packagesEl.__len__())
            for i in range(packagesEl):
                self.assertTrue(keySearch in packagesEl[i].text, "result not contain search string")

    def testStaking(self):
        ## click vào staking
        try:
            time.sleep(2)
            element = getElement(self.driver, self.searchInputEl)

                # do it N time
            with open('testcase.csv', 'r') as file:
                reader = csv.reader(file)
                for keySearch in reader:
                    handleClick(self.driver, self.clearEl)
                    element.send_keys(keySearch)
                    time.sleep(2)
                    emptyEl = getElement(self.driver, self.emptyImgEl)
                    # self.assertEqual(emptyEl.is_displayed(), True, "Failed size is not empty")

                    if emptyEl is None:
                        packagesEl = self.driver.find_elements(by=By.XPATH, value=self.packageEl)
                        
                        print('asdasdasd@@@#@# ', packagesEl.__len__())
                        if packagesEl.__len__() == 0:
                            continue

                        stakingEl = getElement(self.driver, "//div[@class='staking']")
                        print(packagesEl.__len__(), keySearch[0], ': https://github.com/Sonek-HoangBui/demo-ut/blob/main/unittest/demo.py#L83')
                        stakingEl.screenshot(keySearch[0] +'_'+str(packagesEl.__len__())+'.png')
                        for i in range(packagesEl.__len__()):
                            self.assertTrue(keySearch[0].lower() not in packagesEl[i].text.lower(), "result not contain search string")

        except Exception as ex:
            # sleep 5s to retry
            print(ex)
            # element = self.driver.find_element(by=By.XPATH,value=self.showStakeInfoBtnEl)
            # element.click()

if __name__ == '__main__':
   unittest.main()
