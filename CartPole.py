import gym
import numpy as np

env = gym.make('Cartpole-v1')
for i_episode in range(100):
    obsv = env.reset()
    for t in range(100):
        env.render()
        action = env.action_space.sample()
        obsv, reward, done, info = env.step(action)
        if done:
            reward = reward + 1000
            print("Episode finished after {} timesteps".format(t+1))
        else: 
            reward = reward - 10
            break
env.close()