'''
Created on Feb 24, 2026

@author: kd00250
'''

from server import server 

class local_server(server):
    """
    handles basic communication with the server
    """
    
    def send(self, request: str) -> str:
        """
        pretends to send requests to the server
        
        Args:
            request: Should contain two parts a username followed by a
                     password, separated by a comma.
        
        Returns:
            "ok" if username/password combo are valid.
            "not ok" if username/password combo are invalid.
        """
        parts = request.split(",")
        if len(parts) == 2 and parts[0] == parts[1]:
            return "ok"
        else:
            return "not ok"
        
