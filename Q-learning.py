import numpy as np
if not hasattr(np, 'bool8'):
    np.bool8 = np.bool_
import gym
import time

env = gym.make("CartPole-v1", render_mode=None)

def generate_bins():
    bins_num = 24
    bins = [
        np.linspace( -2.4, 2.4, bins_num),
        np.linspace( -3.0, 3.0, bins_num),
        np.linspace( -0.5, 0.5, bins_num),
        np.linspace( -2.0, 2.0, bins_num)
    ]
    return bins

def discretize_state(state, bins):
    discretized = []
    for i in range(len(state)):
        discretized.append(np.digitize(state[i], bins[i]) - 1)
    return tuple(discretized)

bins = generate_bins()

qtable_shape = (len(bins[0]) + 1, len(bins[1]) + 1, len(bins[2]) + 1, len(bins[3]) + 1, env.action_space.n)
qtable = np.zeros(qtable_shape)

a = 0.1
d = 0.9
e = 1.0
decay = 0.9995
min_epsilon = 0.1
num_episode = 100000

scores = []
for episode in range(num_episode) : 
    if episode == 99900:
        env.close()
        env = gym.make("CartPole-v1", render_mode="human")
    observation, info = env.reset()
    state = discretize_state(observation, bins)
    done = False
    score = 0
    
    while not done:
        # time.sleep(0.02)
        if np.random.random() < e:
            action = env.action_space.sample()
        else:
            action = np.argmax(qtable[state])
        
        new_observation, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        new_state = discretize_state(new_observation, bins)
        
        current_q = qtable[state][action]
        max_futureq = np.max(qtable[new_state])
        new_q = current_q + a * (reward + d * max_futureq - current_q)
        qtable[state][action] = new_q
        state = new_state
        score += reward
    e = max(min_epsilon, e * decay)
    scores.append(score)
    
    if episode % 100 == 0:
        print(f"Episode {episode}, Score: {score}, Epsilon: {e}")

env.close()
avg_score = np.mean(scores[-100:])
print(f"Average score over last 100 episodes: {avg_score}")
