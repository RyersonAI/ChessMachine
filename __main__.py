from Agent.agent import Agent
from lcztools import LeelaBoard
import Vision
import Robot 


def main():

    board = LeelaBoard()
    agent = Agent()
    vision = Vision()
    robot = Robot()

    state0 = vision.initial_state # state is np array of shape (height, width, color_channels)

    # Main game loop 

    while True:

        # Wait for player to make a move
        while True:

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
        agent_move = agent.model.predict(board)

        # Make agent move on internal board
        board.move(agent_move)

        # Make the agent move on the physical board
        robot.arm.make_move(agent_move)
        
        state0 = robot.camera.get_image() 




if __name__ == '__main__':

    main()
