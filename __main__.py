from Agent.kerasNet import KerasNet
from lcztools import LeelaBoard
import Vision
import Robot 


def main():


    board = LeelaBoard()
    agent = KerasNet()

    '''
    vision = Vision()
    robot = Robot()


    # Take inital image of the board 
    # state is np array of shape (height, width, color_channels)
    state0 = robot.camera.get_image()
    
    # Main game loop 

    while True:

        # Wait for player to make a move

        while True:

            #TODO Figure out how to use button with pi 
            if robot.clock.player_pressed:
                break

        state1 = robot.camera.get_image()

        # Determine move made by player using 2 images, 1 taken
        # before move was made, 1 taken after and a list of 

        # all the possible moves they could've made 
        #possible_moves = board.generate_legal_moves()


        player_move = vision.model.predict(state0, state1)

        # Make player move on internal board
        board.move(player_move)

        # Determine the move to make in response 
        agent_move = agent.get_move(board, strengh=1)

        # Make agent move on internal board
        board.move(agent_move)

        # Make the agent move on the physical board
        robot.arm.make_move(agent_move)
        
        state0 = robot.camera.get_image() 

'''



if __name__ == '__main__':

    main()
