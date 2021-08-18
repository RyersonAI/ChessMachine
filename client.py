
import socket
import pickle as pkl 
import numpy as np 

HOST = socket.gethostname()
PORT = 65433
HEADERSIZE = 10

class client:

    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((HOST, PORT))

    def get_board(self, img):

        msg = pkl.dumps(img)
        msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

        self.s.send(msg)

        full_msg = ''
        new_msg = True 

        while True:

            msg = self.s.recv(16)

            if new_msg:

                msg_len = int(msg[:HEADERSIZE])
                new_msg = False 

            full_msg += msg 

            if len(full_msg)-HEADERSIZE == msg_len:
                response = pkl.loads(full_msg)
                break 
    
            
        return response 
