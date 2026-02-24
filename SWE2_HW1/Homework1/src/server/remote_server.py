'''
Created on Feb 23, 2026

@author: kd00250
'''

import zmq 
from server import import server

class remote_server(server):
    """
    handles basic communication with the server
    """
    
    def send(self, request: str) -> str:
        """
        Send request to the server
        
        Args:
            request: Should contain two parts a username followed by a
                     password, separated by a comma.
        
        Returns:
            "ok" if username/password combo are valid.
            "not ok" if username/password combo are invalid.
        """
        
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect("tcp://127.0.0.1:55555")
        socket.send_string(request)
        response = socket.recv_string()
        return response
    