import gym
import matplotlib.pyplot as plt 
import time

# the optional render_mode=human will output the UI for the game
env = gym.make('MountainCar-v0', render_mode='human')

# Observation and action space 
obs_space = env.observation_space
action_space = env.action_space
print("The observation space: {}".format(obs_space))
print("The action space: {}".format(action_space))

# reset the environment and see the initial observation
obs = env.reset()
print("The initial observation is {}".format(obs))

done = False;

total_reward = 0.0;

while not done:
    # time.sleep(0.1)

    # Sample a random action from the entire action space
    random_action = env.action_space.sample()

    # perform the action
    new_obs, reward, done, info, extras = env.step(random_action)
    total_reward += reward;

    print("The new observation is {} with reward {}, total reward: {}".format(new_obs, reward, total_reward))

env.close()
# # Take the action and get the new observation space
# new_obs, reward, done, info = env.step(random_action)
# print("The new observation is {}".format(new_obs))