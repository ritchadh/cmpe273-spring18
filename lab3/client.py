import zmq
import time
import sys
from threading import Thread

context = zmq.Context()

def pushmessages():
    global context
    sock = context.socket(zmq.PUSH)
    sock.connect("tcp://127.0.0.1:1234")
    name = sys.argv[1]
    client_first_connect = True
    if client_first_connect is True:
        print("User[{}] connected to the chat server".format(name))
        client_first_connect = False
    while True:
        msg_pushed = input("[{}]>".format(name))
        sock.send_string('['+ name +']>' + msg_pushed)
        
def subscription():
    global context
    pub = context.socket(zmq.SUB)
    pub.setsockopt_string(zmq.SUBSCRIBE, '')
    pub.connect("tcp://127.0.0.1:7890")
    while True:
        responseserver = pub.recv_string()
        print('\n'  + responseserver)


if __name__ == '__main__':    
    t1 = Thread(target=pushmessages).start()
    t2 = Thread(target=subscription).start()