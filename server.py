from ChessAgent import Agent
from ChessVision import Vision
import socket
from lcztools import LeelaBoard
import pickle as pkl 
import numpy as np 
import os 


agent = Agent()
vision = Vision()

def process_input(model_input):


    #board = vision.get_board(model_input)
    board = LeelaBoard()
    agent_move = agent.get_move(board)
    print('hehe')

    return (board, agent_move)

HOST = socket.gethostname()
PORT = 65433
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

full_msg = b''
new_msg = True 


while True:


    clientSocket, address = s.accept()
    print(f'Connection from {address}')
    msg = clientSocket.recv(16)

    if new_msg:
        print('hello')
        msg_len = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg 

    if len(full_msg)-HEADERSIZE == msg_len:
        print('wabba')
        model_input = pkl.loads(full_msg)
        model_output = process_input(model_input)

        msg = pkl.dumps(model_output)
        msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg

        clientSocket.send(msg)

        new_msg = True
        full_msg = b''











    