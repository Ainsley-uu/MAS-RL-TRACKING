from env import Maze


def update():
    for episode in range(100):
        # initial observation
        observation = env.reset()

        env.render()

    # end of game
    print('game over')
    env.destroy()

if __name__ == "__main__":
    env = Maze()

    env.after(100, update)
    env.mainloop()