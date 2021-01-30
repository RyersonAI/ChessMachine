from lcztools import load_network, LeelaBoard
from keras_net import KerasNet
import policy_index 


net = KerasNet()
board = LeelaBoard()


while  board.is_game_over() == False:

    print(board)
    move_dict = net._evaluate(board)
    for k, v in move_dict[0].items():
        move = k
        break
    board.push_uci(move)

    
print(board)
