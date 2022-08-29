from asyncio import subprocess
import asyncio
from nis import cat
import os
from pickle import TRUE
import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json
from AppKit import NSPasteboard, NSStringPboardType


def getElement(driver, xpath):
    try:
        return driver.find_element(by=By.XPATH,value=xpath)
    except:
        return None

def handleClick(driver, xpath):
    try:
        driver.find_element(by=By.XPATH,value=xpath).click()
    except:
        return None

class SimpleTest(unittest.TestCase):
    domain = "https://dev.nft.mobilelab.vn"
    # domainCollection = "https://dev.nft.mobilelab.vn/collection/383"
    domainCollection = "https://dev.nft.mobilelab.vn/asset?collection_id=620&status=8"

    showStakeInfoBtnEl = "(//button[@type='button'])[2]"
    searchInputEl = "//input[@type='text']"
    emptyImgEl = "//div[@class='ant-empty-image']"
    btnLoginEl = "//span[normalize-space()='Connect Wallet']"
    wcEl = "//span[normalize-space()='WalletConnect']"
    cpBtnEl = "//a[normalize-space()='Copy to clipboard']"
    spanPriceEl = "//span[normalize-space()='Price']"
    buyBtnEl = "//span[normalize-space()='Buy Now']"
    checkoutBtnEl = "//span[normalize-space()='Checkout']"
    apprBtnEl = "//span[normalize-space()='Approve item']"

    def setUp(self):
        print('setUp')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.domain)
        asyncio.run(self.login())
        # with open('session.txt') as f:
        #     session = f.read()
        #     script_session = "window.localStorage.setItem('session',`{0}`);".format(session)
        #     self.driver.execute_script(script_session)
        # self.driver.refresh()

    # def setUpClass():
    #     print('setUpClass')

    # def tearDown(self):
    #     print('tearDown')

    # def tearDownClass():
    #     print('tearDownClass')

    # # def run():
    # #     print('run')
    
    # def skipTest():
    #     print('skipTest')

    # # def shortDescription():
    # #     return 'Test staking'

    # def debug():
    #     return 'debug'
    def testBuyItem(self):
        i = 0
        while i < 20:
            self.buyItem()
            i += 1
            
        

    def buyItem(self):
        element = getElement(self.driver, self.btnLoginEl)
        if element != None:
            self.login()

        self.driver.get(self.domainCollection)
        print('=== testBuyItem ===')
        time.sleep(1)
        y = 200
        # element = getElement(self.driver, self.spanPriceEl)
        while handleClick(self.driver, self.spanPriceEl) is None:
            self.driver.execute_script("window.scrollBy(0, `{0}`)".format(y))
            y += 800
            if y > 8000:
                break
        
        time.sleep(3)
        handleClick(self.driver, self.buyBtnEl)

        if getElement(self.driver, self.apprBtnEl) is not None:
            time.sleep(1)
            handleClick(self.driver, self.apprBtnEl)
            time.sleep(15)
        
        handleClick(self.driver, self.checkoutBtnEl)

        time.sleep(15)
        # element.click()

    async def login(self):
        print('testStaking')
        ## click vào staking
        try:
            cmdRunMobile = "cd /Users/jeff/github/golang-automation && godog --tags=@android --random --format=cucumber"
            procMobile = await asyncio.create_subprocess_shell(
                cmdRunMobile,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE)
            procMobile.communicate()

            time.sleep(1)
            element = self.driver.find_element(by=By.XPATH,value=self.btnLoginEl)
            element.click()

            time.sleep(1)
            element1 = self.driver.find_element(by=By.XPATH, value=self.wcEl)
            element1.click()

            time.sleep(1)
            element2 = self.driver.find_element(by=By.XPATH, value=self.cpBtnEl)
            element2.click()

            pb = NSPasteboard.generalPasteboard()
            pbstring = pb.stringForType_(NSStringPboardType)
            print(pbstring)

            # os.system("cd /Users/jeff/github/golang-automation && godog --tags=@android --random --format=cucumber")
            # cmd = "echo '{0}' > /Users/jeff/github/golang-automation/wc".format(pbstring)
            
            # proc = await asyncio.create_subprocess_shell(
            #     cmd,
            #     stdout=asyncio.subprocess.PIPE,
            #     stderr=asyncio.subprocess.PIPE)

            # proc.communicate()
            # subprocess.create_subprocess_shell("cd /Users/jeff/github/golang-automation && godog --tags=@android --random --format=cucumber")
            # print(f'[{cmd!r} exited with {proc.returncode}]')
            # if stdout:
            #     print(f'[stdout]\n{stdout.decode()}')
            # if stderr:
            #     print(f'[stderr]\n{stderr.decode()}')

            time.sleep(15)
        except Exception as inst:
            # sleep 5s to retry
            print(inst)
            # element = self.driver.find_element(by=By.XPATH,value=self.showStakeInfoBtnEl)
            # element.click()

if __name__ == '__main__':
   unittest.main()
