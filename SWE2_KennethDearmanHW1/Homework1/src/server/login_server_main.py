'''
Created on Feb 23, 2026

@author: kd00250
'''
import zmq

def process_request(request: str) -> str:
    """Process a login request and return a reply."""
    parts = request.split(",")
    if len(parts) == 2 and parts[0] == parts[1] and parts[0] != "":
        return "ok"
    return "not ok"

def main(): 
    """
    Sample Login Server main
    """
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://127.0.0.1:5555")
    
    while True:
        print("Server - Waiting for request")
        request = socket.recv_string()
        print(f"Server - Received : [{request}]")
        
        if request == "exit":
            print("Server - exiting")
            socket.close()
            context.term()
            return 
        
        reply = process_request(request)
        print(f"Server - Replying with : [{reply}]")
        socket.send_string(reply)
        
    socket.close()
    context.term()
    
    
if __name__ == '__main__':
    main()