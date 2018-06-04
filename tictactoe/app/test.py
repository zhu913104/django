from Tic_Tac_Toe import tic_tac_toe
from RL import QLearningTable
import time
import sys

env = tic_tac_toe()
RL_1 = QLearningTable(actions=env.actions,file="OO.csv",e_greedy=1)
RL_2 = QLearningTable(actions=env.actions,file="XX.csv",e_greedy=1)

t=time.time()



def main(env,RL_1,RL_2):
        observation = env.reset().copy()
        player = input()
        while True:
            # fresh env
            if player=="2":
                # RL choose action based on observation
                action_1 = str(RL_1.choose_action(str(observation)))
                # RL take action and get next observation and reward
                observation_, reward_1, done_1,legal_1 = env.step(action_1,observation)
                # make sure RL do the legal step
                while not legal_1:
                    action_1 = RL_1.choose_action(str(observation),legal_1)
                    observation_, reward_1, done_1, legal_1 = env.step(action_1,observation)
                # swap observation
                observation = observation_
                env.render(observation)
                if done_1 :
                    break
                action_1=input()
                observation_, reward_1, done_1,legal_1 = env.step(action_1,observation)
                # make sure RL do the legal step
                while not legal_1:
                    action_1 = input()
                    observation_, reward_1, done_1, legal_1 = env.step(action_1,observation)
                    print("rere")
                observation = observation_
                env.render(observation)
                if done_1 :
                    break

            if player=="1":

                action_1=input()
                observation_, reward_1, done_1,legal_1 = env.step(action_1,observation)
                # make sure RL do the legal step
                while not legal_1:
                    action_1 = input()
                    observation_, reward_1, done_1, legal_1 = env.step(action_1,observation)
                    print("rere")
                observation = observation_
                env.render(observation)
                if done_1 :
                    break
                # RL choose action based on observation
                action_2 = str(RL_2.choose_action(str(observation)))
                # RL take action and get next observation and reward
                observation_, reward_2, done_2, legal_2 = env.step(action_2,observation)
                # make sure RL do the legal step
                while not legal_2 :
                    action_2 = RL_2.choose_action(str(observation),legal_2)
                    observation_, reward_2, done_2, legal_2 = env.step(action_2,observation)
                # swap observation
                observation = observation_
                env.render(observation)

                # break while loop when end of this episode
                if done_2 :
                    break


    # end of game



if __name__ == "__main__":
    # maze game
    main(env,RL_1,RL_2)