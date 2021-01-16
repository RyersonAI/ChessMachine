# I'm not 100% sure about the interface between python and unity using ml-agents
# so it might not be exactly like it is below but this is roughly what our code is 
# going to look like 

from mlagents_envs.environment import UnityEnvironment

env = UnityEnvironment(file_name="ChessVisionDataGenerator")

# action -> env -> 1 image (height x width x color_channels)

# env.reset returns an image of the inital board 
# the unity game only outputs images of the board 
# and only receives actions in uci format as input


def generate_training_batch(game_history):
    # game history is a list of uci moves taken in a game 
    # ex. game_history = ['e2e4', 'e7e5', 'd2d4', ....]
    
    training_data = []
    state0 = env.reset()
    
    for move in game_history:
        state1 = env.step(move)
        
        # training_sample = [model_input, model_output]
        training_sample = [(state0, state1), move] 
        training_data.append(training_sample)
        
        # The next state becomes the current state at the next timestep so ...
        state0 = state1
        
    return training_data
