'''
Created on Feb 24, 2026

@author: kd00250
'''
import unittest, time, zmq
from server.login_server_main import process_request 
from threading import Thread
from server.login_server_main import main

class Test(unittest.TestCase):

    def setUp(self):
        serverThread = Thread(target=main)
        serverThread.start()
        time.sleep(1)
        context = zmq.Context()
        self._socket = context.socket(zmq.REQ)
        self._socket.connect("tcp://127.0.0.1:5555")
        
    def tearDown(self):
        self._socket.send_string("exit")
    
    def testMatchingParts(self):
        self._socket.send_string("hello,hello")
        response = self._socket.recv_string()
        self.assertEqual("ok", response)
        
    def testNonMatchingParts(self):
        self._socket.send_string("hello,world")
        response = self._socket.recv_string()
        self.assertEqual("not ok", response)
        
    def testEmptyString(self):
        self._socket.send_string(",")
        response = self._socket.recv_string()
        self.assertEqual("not ok", response)
        
    def testPartOneEmptyString(self):
        self._socket.send_string("aaa,")
        response = self._socket.recv_string()
        self.assertEqual("not ok", response)
        
    def testPartTwoEmptyString(self):
        self._socket.send_string(",aaa")
        response = self._socket.recv_string()
        self.assertEqual("not ok", response)
        
    
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
    
    def test_exit_branch(self):
        self.assertEqual(process_request("exit"), "not ok")
        

if __name__ == "__main__":
    unittest.main()