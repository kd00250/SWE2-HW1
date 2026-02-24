'''
Created on Feb 23, 2026

@author: kd00250
'''

from abc import ABC, abstractmethod

class Server(ABC):
    """
    handles communication  with the server
    """
    
    @abstractmethod
    def send(self, request: str) -> str:
        """
        Sends request to the server
        
         Args:
            request: Should contain two parts a username followed by a 
                     password, separated by a comma.
        
        Returns:
            "ok" if username/password combo are valid.
            "not ok" if username/password combo are invalid.
        """
        
        pass
        
