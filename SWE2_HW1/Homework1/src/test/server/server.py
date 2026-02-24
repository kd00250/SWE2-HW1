'''
Created on Feb 24, 2026

@author: kd00250
'''
import unittest
from login_server_main import process_request 

class Test(unittest.TestCase):


    def test_valid_login(self):
        self.assertEqual(process_request("admin,admin"), "ok")

    def test_invalid_password(self):
        self.assertEqual(process_request("admin,wrongpassword"), "not ok")
        
    def test_missing_password(self):
        self.assertEqual(process_request("admin"), "not ok")
        
    def test_empty_request(self):
        self.assertEqual(process_request(""), "not ok")
        
    def test_extra_parts(self):
        self.assertEqual(process_request("admin,admin,extra"), "not ok")

if __name__ == "__main__":
    unittest.main()