import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import numpy as np
from conways_game_of_life import logger

class GameController:
    def __init__(self, model, view, save=False):
        self.model = model
        self.view = view
        self.save = save
        self.cid = None

    def get_initial_state(self):
        self.view.axis.set_title('Click to activate cell, Double click to end')
        self.cid = self.view.fig.canvas.mpl_connect('button_press_event', self.onclick)
        plt.show(block=True)
        
    def onclick(self, event):
        if event.xdata is not None and event.ydata is not None:
            i, j = int(np.floor(event.ydata + 0.5)), int(np.floor(event.xdata + 0.5))
            self.view._initial_state[i, j] = not self.view._initial_state[i, j]
            self.view.img.set_data(self.view._initial_state)
            plt.draw()
        if event.dblclick:
            self.view.fig.canvas.mpl_disconnect(self.cid)
            self.model.state = self.view._initial_state
            self.run()

    def run(self):
        def animate(i):
            state = self.model.update()
            self.view.display(state, self.model.generations)
        
        ani = animation.FuncAnimation(self.view.fig, animate, interval=100)
        plt.show()
        
        if self.save:
            logger.info('Saving animation')
            ani.save('animation.gif', writer='imagemagick', fps=10)


