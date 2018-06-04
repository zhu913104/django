import os
import time
import numpy as np
class tic_tac_toe(object):
    def __init__(self):
        self.status=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.player = ['1','2']
        self.turn=0
        self.round=0
        self.actions=['1','2','3','4','5','6','7','8','0']
        self.done = False

    def reset(self):
        self.status = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.turn=0
        self.round=0
        self.done = False
        return self.status

    def checkgame(self,status):
        for i in range(3):
            if status[i] == status[i+3] == status[i+6] == self.turn:
                return True
            elif status[i*3] == status[i*3+1] == status[i*3+2] == self.turn:
                return True
        if status[0] == status[4] == status[8] == self.turn or status[2] == status[4] == status[6] == self.turn:
            return True
        return False

    def render(self,status):
        os.system("cls")
        print("")
        tran=status.copy()
        for i in range(len(tran)) :
            if tran[i] == '1':
                tran[i]= 'O'
            elif tran[i]=='2':
                tran[i]= 'X'
        for i in range(3):
            print('  ' + tran[i*3] + "|" + tran[i*3+1] + '|' + tran[i*3+2])

    def step(self,action,status):
        self.turn=self.player[self.round%2]
        action = int(action)
        self.leg=False
        status_=status.copy()
        r=0
        if status_[action] == " ":
            status_[action] = self.turn
            self.round+=1
            self.leg = True
            if self.checkgame(status_) :
                r=10
                self.done = True
                self.leg= True

            return status_ ,r,self.done, self.leg
        else:
            if  " "not in status:
                self.done = True
                self.leg = True
            return status ,r,self.done, self.leg


    # def main(self):
    #     self.render()
    #     print(self.status)
    #     if self.gamemode=='man2ran':
    #         if (self.round%2==0):
    #             action=input()
    #         else:
    #             action=np.random.randint(1,9)
    #     elif self.gamemode=='ran2rand':
    #         if (self.round%2==0):
    #             action=np.random.randint(1,10)
    #             print(action)
    #         else:
    #             action=np.random.randint(1,10)
    #             print(action)
    #     elif self.gamemode=='man2man':
    #         if (self.round%2==0):
    #             action = input()
    #         else:
    #             action = input()
    #
    #     self.update(action)
    #     if self.checkgame() :#其中一方獲勝
    #         os.system("cls")
    #         print("{} WIN!!!".format(self.turn))
    #         time.sleep(2)
    #         self.render()
    #         print("\n-------------------------\n")
    #         self.reset()
    #     elif self.round==9:#和局
    #         os.system("cls")
    #         print("TOE")
    #         time.sleep(2)
    #         self.render()
    #         print("\n-------------------------\n")
    #         self.reset()


#
# game = tic_tac_toe(gamemode='man2man')
# while __name__ == '__main__':
#     game.main()