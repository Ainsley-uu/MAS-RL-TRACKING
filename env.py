import numpy as np
import time
import sys
import tkinter as tk

from maze_env import MAZE_H

UNIT = 40
MAZE_H = 20
MAZE_W = 20

class Maze(tk.Tk, object):
    def __init__(self):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('maze')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_H * UNIT))
        self._build_maze()
    
    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='white',
                           height=MAZE_H * UNIT,
                           width=MAZE_W * UNIT)

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        # create origin
        origin = np.array([20, 20])

        # hell
        hell1_center = origin + np.array([UNIT * 17, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 20, hell1_center[1] - 20,
            hell1_center[0] + 20, hell1_center[1] + 20,
            fill='black')
        hell1_center = origin + np.array([UNIT * 17, UNIT * 2])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 20, hell1_center[1] - 20,
            hell1_center[0] + 20, hell1_center[1] + 20,
            fill='black')
        hell1_center = origin + np.array([UNIT * 18, UNIT])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 20, hell1_center[1] - 20,
            hell1_center[0] + 20, hell1_center[1] + 20,
            fill='black')
        hell1_center = origin + np.array([UNIT * 18, UNIT * 2])
        self.hell1 = self.canvas.create_rectangle(
            hell1_center[0] - 20, hell1_center[1] - 20,
            hell1_center[0] + 20, hell1_center[1] + 20,
            fill='black')

        # hell
        hell2_center = origin + np.array([UNIT * 13, UNIT * 8])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 20, hell2_center[1] - 20,
            hell2_center[0] + 20, hell2_center[1] + 20,
            fill='black')
        hell2_center = origin + np.array([UNIT * 13, UNIT * 9])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 20, hell2_center[1] - 20,
            hell2_center[0] + 20, hell2_center[1] + 20,
            fill='black')
        hell2_center = origin + np.array([UNIT * 14, UNIT * 8])
        self.hell2 = self.canvas.create_rectangle(
            hell2_center[0] - 20, hell2_center[1] - 20,
            hell2_center[0] + 20, hell2_center[1] + 20,
            fill='black')

        # hell
        hell3_center = origin + np.array([UNIT * 2, UNIT * 2])
        self.hell3 = self.canvas.create_rectangle(
            hell3_center[0] - 20, hell3_center[1] - 20,
            hell3_center[0] + 20, hell3_center[1] + 20,
            fill='black')
        
        # hell
        hell4_center = origin + np.array([UNIT * 7, UNIT * 8])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 20, hell4_center[1] - 20,
            hell4_center[0] + 20, hell4_center[1] + 20,
            fill='black')
        hell4_center = origin + np.array([UNIT * 7, UNIT * 9])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 20, hell4_center[1] - 20,
            hell4_center[0] + 20, hell4_center[1] + 20,
            fill='black')
        hell4_center = origin + np.array([UNIT * 8, UNIT * 9])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 20, hell4_center[1] - 20,
            hell4_center[0] + 20, hell4_center[1] + 20,
            fill='black')
        hell4_center = origin + np.array([UNIT * 8, UNIT * 8])
        self.hell4 = self.canvas.create_rectangle(
            hell4_center[0] - 20, hell4_center[1] - 20,
            hell4_center[0] + 20, hell4_center[1] + 20,
            fill='black')

        # hell
        hell5_center = origin + np.array([UNIT * 3, UNIT * 18])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 20, hell5_center[1] - 20,
            hell5_center[0] + 20, hell5_center[1] + 20,
            fill='black')
        hell5_center = origin + np.array([UNIT * 3, UNIT * 17])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 20, hell5_center[1] - 20,
            hell5_center[0] + 20, hell5_center[1] + 20,
            fill='black')
        hell5_center = origin + np.array([UNIT * 4, UNIT * 18])
        self.hell5 = self.canvas.create_rectangle(
            hell5_center[0] - 20, hell5_center[1] - 20,
            hell5_center[0] + 20, hell5_center[1] + 20,
            fill='black')

        # create prey
        prey_center = origin + np.array([UNIT * 0, UNIT * 0])
        self.prey = self.canvas.create_oval(
            prey_center[0] - 15, prey_center[1] - 15,
            prey_center[0] + 15, prey_center[1] + 15,
            fill='red')
    
        # create hunter
        hunter1_center = origin + np.array([UNIT * 5, UNIT * 5])
        self.hunter1 = self.canvas.create_oval(
            hunter1_center[0] - 15, hunter1_center[1] - 15,
            hunter1_center[0] + 15, hunter1_center[1] + 15,
            fill='yellow')

       # create hunter
        hunter2_center = origin + np.array([UNIT * 15, UNIT * 15])
        self.hunter2 = self.canvas.create_oval(
            hunter2_center[0] - 15, hunter2_center[1] - 15,
            hunter2_center[0] + 15, hunter2_center[1] + 15,
            fill='yellow')

        # create hunter
        hunter3_center = origin + np.array([UNIT * 3, UNIT * 13])
        self.hunter3 = self.canvas.create_oval(
            hunter3_center[0] - 15, hunter3_center[1] - 15,
            hunter3_center[0] + 15, hunter3_center[1] + 15,
            fill='yellow')

        # pack all
        self.canvas.pack()
    
    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.hunter1)
        self.canvas.delete(self.hunter2)
        self.canvas.delete(self.hunter3)
        origin = np.array([20,20])

        hunter1_center = origin + np.array([UNIT * 5, UNIT * 5])
        self.hunter1 = self.canvas.create_oval(
            hunter1_center[0] - 15, hunter1_center[1] - 15,
            hunter1_center[0] + 15, hunter1_center[1] + 15,
            fill='yellow')

        hunter2_center = origin + np.array([UNIT * 15, UNIT * 15])
        self.hunter2 = self.canvas.create_oval(
            hunter2_center[0] - 15, hunter2_center[1] - 15,
            hunter2_center[0] + 15, hunter2_center[1] + 15,
            fill='yellow')

        hunter3_center = origin + np.array([UNIT * 3, UNIT * 13])
        self.hunter3 = self.canvas.create_oval(
            hunter3_center[0] - 15, hunter3_center[1] - 15,
            hunter3_center[0] + 15, hunter3_center[1] + 15,
            fill='yellow')

        # return observation
        return self.canvas.coords(self.hunter1),self.canvas.coords(self.hunter2) ,self.canvas.coords(self.hunter3)


    def step(self, action):

        action = np.array([0, 0])
        count = 0
        if( action[0] >= (MAZE_W - 1) * UNIT and action[0] <= UNIT):
            count += 1
        if( count % 2 == 0 ):
            action[0] += UNIT
        else:
            action[0] -= UNIT
        self.canvas.move(self.prey, action[0], action[1] )

        s = self.canvas.coords(self.hunter1)
        base_action = np.array([0, 0])
        if action == 0: # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 2:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 3:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT
        
        s_ = self.canvas.coords(self.hunter1)  # next state

        if s_ == self.canvas.coords(self.prey):
            reward = 1
            done = True
            s_ = 'terminal'
        elif s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2) , self.canvas.coords(self.hell3)]:
            reward = -1
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False
        
        return s_, reward, done
    
    def render(self):
        time.sleep(0.05)
        self.update()

if __name__ == "__main__":
    env = Maze()
    env.mainloop()