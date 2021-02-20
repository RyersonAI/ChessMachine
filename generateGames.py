from Agent import keras_net
from lcztools import LeelaBoard 
import random

num_games_per_batch = 32 
net = keras_net.KerasNet()

# Generate games 

batch = []

for g in range(num_games_per_batch):
    
    board = LeelaBoard()
    history = []

    while board.is_game_over() == False:
        
        move_dict = net._evaluate(board)
        move = random.sample(list(move_dict)[:5], 1)[0]
        
        board.push_uci(move)
        history.append(move)
        
    batch.append(history)

# Write games to csv file 

with open('games_sample', 'a') as f:

    for game in batch:

        f.write('START')

        for move in game:
            f.write(',' + move)

        f.write(',END\n')


    


    
