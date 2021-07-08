
import Robot 
import socket


def get_action():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect('localhost', 80)

    
def main():
    
    robot = Robot()

    #TODO connect to remote machine using sockets

    while True:

        # Wait for player to make a move

        while True:

            #TODO Figure out how to use button with pi 
            if robot.clock.player_pressed:
                break

        board_image = robot.camera.get_image()

        # all the possible moves they could've made 
        #possible_moves = board.generate_legal_moves()

        action = get_action(board_image)

        # Make the agent move on the physical board
        robot.arm.make_move(action)
        
       




if __name__ == '__main__':

    main()
