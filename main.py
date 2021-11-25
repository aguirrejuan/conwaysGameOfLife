#! python3
"""
Conway's Game of Life.

Script to simulate Conway's Game of Life.

Usage:
    main.py [--initialize --save_gif]

Options: 
    --save_gif      Save gif after closing animation. [default: False]
    --initialize    Select initial state by hand. [default: False]
"""
import docopt

import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib import style
from numpy import random

from scipy import signal
import numpy as np 



class GameLife:
    """ World where the cells live. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    """
    def __init__(self,initial_state):
        self.state = initial_state
        self._kernel = np.ones((3,3))
        self._kernel[1,1] = 0 
        self.generations = 0 
        self.current_population = np.sum(self.state)
        
    def _rules(self, sum_neighbors:np.array) -> np.array:
        """ Rules of Conway's game of life.
            1. Any live cell with two or three live neighbours survives.
            2. Any dead cell with three live neighbours becomes a live cell.
            3. All other live cells die in the next generation.
               Similarly, all other dead cells stay dead.
        """
        next_state = np.zeros_like(self.state, dtype=bool) # All deads
        alives = self.state == True 
        two_three_neig = (sum_neighbors == 2 )  | (sum_neighbors ==3)
        three_neig = sum_neighbors ==3
        next_state[alives & two_three_neig] = True  # Rule 1 
        next_state[~alives & three_neig] = True    # Rule 2
        return next_state

    def update(self):
        sum_neighbors =  signal.convolve2d(self.state,
                                            self._kernel,
                                            mode='same',)
        
        self.state = self._rules(sum_neighbors)
        self.generations += 1
        self.current_population = np.sum(self.state)

        return self.state


class Interface:
    def __init__(self,save=False, random=True):

        self._initial_state =  random*np.random.normal(loc=0.0,scale=1.0,size=(100,150)) < 0.0
        self.fig, self.axis = plt.subplots(1,1)
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
        self.img = self.axis.imshow(self._initial_state, vmin=0, vmax=1, cmap='plasma')
        self.axis.axis('off')

        self.save = save
        _ = self.run() if random else self.get_initial_state()
        
    def get_initial_state(self,):
        self.axis.set_title(f'Click to activate cell,Double click to end')
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

    def onclick(self,event):
        if event.xdata != None and event.ydata != None:
            i,j = np.floor(event.ydata+0.5), np.floor(event.xdata+0.5)
            i,j = int(i), int(j)    
            self._initial_state [i,j] = ~self._initial_state [i,j]
            self.img.set_data(self._initial_state)
            plt.draw()
            
        if event.dblclick:
            self.fig.canvas.mpl_disconnect(self.cid)
            self.run()

    def run(self,):
        game = GameLife(self._initial_state)
        def animate(i):
            state = game.update()
            self.img.set_data(state)
            self.axis.set_title(f'Generations: {game.generations}')

        ani = animation.FuncAnimation(self.fig, animate, interval=100)
        plt.show()
        if self.save:
            print('Saving...')
            ani.save('animation.gif', writer='imagemagick', fps=10)
        


def main(args):
    save = args['--save_gif']
    random = not args['--initialize']
    interface = Interface(save,random)
    plt.show()
    

if __name__ == "__main__":
    args = docopt.docopt(__doc__)
    main(args)



    
    


    




