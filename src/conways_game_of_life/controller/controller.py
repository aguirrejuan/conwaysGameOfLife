import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from loguru import logger

from conways_game_of_life.controller.protocols import Model, View


class GameController:
    def __init__(self, model: Model, view: View, save: bool = False):
        self.model = model
        self.view = view
        self.save = save
        self.cid = None

    def get_initial_state(self):
        self.view.set_title("Click to activate cell, Double click to end")
        self.cid = self.view.connect_event("button_press_event", self.onclick)
        self.view.show(block=True)

    def onclick(self, event):
        if event.xdata is not None and event.ydata is not None:
            i, j = int(np.floor(event.ydata + 0.5)), int(np.floor(event.xdata + 0.5))
            self.view.update_initial_state(i, j)
            self.view.refresh()
        if event.dblclick:
            self.view.disconnect_event(self.cid)
            self.model.state = self.view.get_initial_state()
            self.run()

    def run(self):
        def animate(i):
            state = self.model.update()
            self.view.display(state, self.model.generations)

        ani = animation.FuncAnimation(self.view.get_figure(), animate, interval=100)
        self.view.show()
        plt.show()

        if self.save:
            logger.info("Saving animation")
            ani.save("animation.gif", writer="imagemagick", fps=10)

        # Keep a reference to the animation to prevent it from being garbage collected
        self.ani = ani
