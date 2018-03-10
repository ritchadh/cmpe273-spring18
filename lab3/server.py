import zmq
import sys

def pullmessages():
    context = zmq.Context()
    sock = context.socket(zmq.PULL)
    sock.bind("tcp://127.0.0.1:1234")  
    pub = context.socket(zmq.PUB)
    pub.bind("tcp://127.0.0.1:7890")
    while True:
        pulledmessage = sock.recv_string()
        pub.send_string(pulledmessage)
        
if __name__ == '__main__':    
    pullmessages()
    