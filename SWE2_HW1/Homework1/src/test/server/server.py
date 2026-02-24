'''
Created on Feb 24, 2026

@author: kd00250
'''
import unittest
from unittest.mock import patch, MagicMock
from server.login_server_main import process_request 
from server.login_server_main import main

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
    
    def test_exit_branch(self):
        self.assertEqual(process_request("exit"), "not ok")
        
    @patch('server.login_server_main.zmq')
    def test_main_invalid_message(self, mock_zmq): 
        mock_context = MagicMock()
        mock_socket = MagicMock()
        mock_zmq.Context.return_value = mock_context
        mock_context.socket.return_value = mock_socket
        
        mock_socket.recv_string.side_effect = ["admin,wrongpassword", "exit"]
        
        main()
        
        mock_socket.send_string.assert_called_once_with("not ok")
        mock_socket.close.assert_called_once()
        mock_context.term.assert_called_once()
        
    @patch('server.login_server_main.zmq')
    def test_main_exit_immediately(self, mock_zmq):
        """Exit on first message — covers bind, recv, exit branch, close, term."""
        mock_context = MagicMock()
        mock_socket = MagicMock()
        mock_zmq.Context.return_value = mock_context
        mock_context.socket.return_value = mock_socket

        mock_socket.recv_string.side_effect = ["exit"]

        main()

        mock_socket.bind.assert_called_once_with("tcp://127.0.0.1:5555")
        mock_socket.close.assert_called_once()
        mock_context.term.assert_called_once()

    @patch('server.login_server_main.zmq')
    def test_main_processes_request_then_exits(self, mock_zmq):
        """One normal request then exit — covers send_string path too."""
        mock_context = MagicMock()
        mock_socket = MagicMock()
        mock_zmq.Context.return_value = mock_context
        mock_context.socket.return_value = mock_socket

        mock_socket.recv_string.side_effect = ["admin,admin", "exit"]

        main()

        mock_socket.send_string.assert_called_once_with("ok")
        mock_socket.close.assert_called_once()
        mock_context.term.assert_called_once()

if __name__ == "__main__":
    unittest.main()