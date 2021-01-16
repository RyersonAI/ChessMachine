from keras_net import KerasNet 
import policy_index as policy_index


class Agent():

	def __init__(self):

		self.policy_index = policy_index.policy_index
		self.net = KerasNet()


	def get_move(self, board):

		policy, value = self.net.evaluate(board)
		move_idx = np.argmax(policy)
		move_uci = self.policy_index[move_idx]

		return move_uci

