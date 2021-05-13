from tqdm import tqdm
import os
import os.path as osp
import pickle
import numpy as np
import gym
import sys
import time
from rlpyt.agents.pg.categorical import CategoricalPgAgent
from Network import *
from collections import namedtuple

def main () : 
    env = gym.make('Acrobot-v1')
    EnvSpace = namedtuple('EnvSpace', ['action', 'observation'])
    agent_dict = torch.load('a2c_acrobot/run_0/itr_147499.pkl')
    state_dict = agent_dict["agent_state_dict"]
    agent = CategoricalPgAgent(AcrobotNet)
    agent.initialize(EnvSpace(env.action_space, env.observation_space))
    agent.load_state_dict(state_dict)
    done = False
    trajectory = []
    s = torch.tensor(env.reset()).float()
    a = torch.tensor(0)
    r = torch.tensor(0).float()
    i = 0
    while not done : 
        i += 1
        env.render()
        a = agent.step(s, a, r).action
        s_, r, done, info = env.step(a.item())
        s_ = torch.tensor(s_).float()
        r = torch.tensor(r).float()
        s = s_
        time.sleep(0.05)
    print(f'Finished Episode in {i} steps')
    env.close()

if __name__ == "__main__" : 
    main ()
