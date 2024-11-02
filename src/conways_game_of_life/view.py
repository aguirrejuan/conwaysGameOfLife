import matplotlib.pyplot as plt 
import numpy as np

class Interface:
    def __init__(self, initial_state):
        self._initial_state = initial_state
        self.fig, self.axis = plt.subplots(1, 1)
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
        self.img = self.axis.imshow(self._initial_state, vmin=0, vmax=1, cmap='plasma')
        self.axis.axis('off')

    def display(self, state, generations):
        self.img.set_data(state)
        self.axis.set_title(f'Generations: {generations}')
        plt.draw()