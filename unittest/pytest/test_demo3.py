# from asyncio import subprocess
# import asyncio
# from cmath import log
# from nis import cat
# import os
# from pickle import TRUE
# import time
import unittest
import eth_keys, os
from web3 import Web3
import hashlib
import requests
import binascii
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




# export default {
# 	PHASE: "bring discover dynamic town helmet rhythm sunset neither history tooth lecture buyer",
# 	BASE_URL: "https://dev.api.trustkeys.network/v1/game-guild",
# 	PUBK: "036039bd43015f480c694f2a5c1b0941b37271c18616135c59c2cef9849abb7447",
# 	PRIVK: "5edd050a7c6c9eca1d3b6866732525685dffb9c7dc52eef675f096459b3ba39a",
# 	ADDR: "0x497789F26dcCFf507cb020c2554130E195536F2C",
# 	OFFSET: 0,
# 	LIMIT: 10,
# }


def sha3_256Hash(msg):
    return hashlib.sha256(msg.encode("utf8")).digest()

class GameGuild(unittest.TestCase):
    domain = "https://dev.nft.mobilelab.vn"
    # domainCollection = "https://dev.nft.mobilelab.vn/collection/383"
    domainCollection = "https://dev.nft.mobilelab.vn/collection/554"
    priv = "0x5edd050a7c6c9eca1d3b6866732525685dffb9c7dc52eef675f096459b3ba39a"
    pubk = "036039bd43015f480c694f2a5c1b0941b37271c18616135c59c2cef9849abb7447"
    addr = "0x497789F26dcCFf507cb020c2554130E195536F2C"

    # def setUpModule(self):
    #     print('setUpModule')
    # def tearDownModule(self):
    #     print('setUpModule')
    def setUp(self):
        print('setUp')

    def testSign1(self):
        print('test sign1')

    def testSign(self):
        # print('test sign')
        # # Generate the private + public key pair (using the secp256k1 curve)
        # signerPrivKey = eth_keys.keys.PrivateKey(bytes.fromhex(self.priv[2:]))
        # # signerPubKey = signerPrivKey.public_key
        # w3 = Web3(Web3.HTTPProvider("https://ropsten.infura.io/v3/1a2db0c6b6eb4514b86afde0ebb8780d"))
        # PA = w3.eth.account.from_key(self.priv)
        # address = PA.address
        # print(address)
        # hashMessage = sha3_256Hash("hi")
        # print(binascii.hexlify(hashMessage), ": hashMessage")
        # signMessage = signerPrivKey.sign_msg_hash(hashMessage)
        # print(signMessage.__str__()[2:], ": signMessage")
        # sign = signMessage.__str__()[2:]
        # BASE_URL = "https://dev.api.trustkeys.network/v1/game-guild"
        # response = requests.get(
        #     f'{BASE_URL}/post/list-post-group?groupID=146&pubkey={self.pubk}&offset=0&limit=10&sign={sign}'
        # )

        # print(response.json())
        # false
        # self.assertLessEqual(response.json()['total'], 1)
        # true
        # self.assertGreaterEqual(response.json()['total'], 1)
        # true
        self.assertEqual(1, 1)
        # false
        self.assertEqual(1, 2)

        # const respGet = http.get(`${consts.BASE_URL}/post/list-post-group?groupID=146&pubkey=${consts.PUBK}&offset=${consts.OFFSET}&limit=${consts.LIMIT}&sign=${sign}`,
		# { headers: { "Content-Type": "application/json" }});
        # print('Private key (64 hex digits):', signerPrivKey)
        # print('Public key (uncompressed, 128 hex digits):', signerPubKey)

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
    # def test_false(self):
    #     self.assertEqual(1, 2)
    # def test_true(self):
    #     self.assertEqual(1, 1)
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