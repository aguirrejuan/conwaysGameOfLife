import matplotlib.pyplot as plt
import numpy as np


class Interface:
    def __init__(self, initial_state):
        self._initial_state = initial_state
        self.fig, self.axis = plt.subplots(1, 1)
        self.fig.subplots_adjust(
            left=0, bottom=0, right=1, top=1, wspace=None, hspace=None
        )
        self.img = self.axis.imshow(self._initial_state, vmin=0, vmax=1, cmap="plasma")
        self.axis.axis("off")

    def set_title(self, title: str) -> None:
        self.axis.set_title(title)

    def connect_event(self, event_name: str, callback) -> int:
        return self.fig.canvas.mpl_connect(event_name, callback)

    def disconnect_event(self, cid: int) -> None:
        self.fig.canvas.mpl_disconnect(cid)

    def show(self, block: bool = False) -> None:
        plt.show(block=block)

    def update_initial_state(self, i: int, j: int) -> None:
        self._initial_state[i, j] = not self._initial_state[i, j]

    def refresh(self) -> None:
        self.img.set_data(self._initial_state)
        plt.draw()

    def get_initial_state(self) -> np.ndarray:
        return self._initial_state

    def get_figure(self):
        return self.fig

    def display(self, state, generations):
        self.img.set_data(state)
        self.axis.set_title(f"Generations: {generations}")
        plt.draw()
