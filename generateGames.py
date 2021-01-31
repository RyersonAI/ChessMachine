from Agent import keras_net
from lcztools import LeelaBoard 


num_games_per_batch = 1 
net = keras_net.KerasNet()

batch = []

for g in range(num_games_per_batch):
    
    board = LeelaBoard()
    history = []

    while board.is_game_over() == False:
        move = net.get_move(board)
        board.push_uci(move)
        history.append(move)
        
    batch.append(history)

with open('games/sample', 'w') as f:

    for game in batch:

        f.write('START\n')

        for move in game:
            f.write(move+'\n')

        f.write('END\n')


    


    
