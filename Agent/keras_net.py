import yaml
import tfprocess

class KerasNet:

    def __init__(self, model_file="128x10-t60-2-5300.pb.gz", cfg_file="configs/128x10-t60-2.yaml"):

        with open(cfg_file, "rb") as f:
            cfg = f.read()

        cfg = yaml.safe_load(cfg)
        print(yaml.dump(cfg, default_flow_style=False))

        tfp = tfprocess.TFProcess(cfg)
        tfp.init_net_v2()
        tfp.replace_weights_v2(model_file)

        self.model = tfp.model 

    def evaluate(self, leela_board):

        input_planes = leela_board.lcz_features()
        model_input = input_planes.reshape(1, 112, 64)
        policy, value, _ = self.model.predict(model_input)
    
        return policy, value


net = KerasNet()