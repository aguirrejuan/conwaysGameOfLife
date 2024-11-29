import numpy as np
from scipy import signal


class GameLife:
    """World where the cells live. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life"""

    def __init__(self, initial_state):
        self.state = initial_state
        self._kernel = np.ones((3, 3))
        self._kernel[1, 1] = 0
        self.generations = 0
        self.current_population = np.sum(self.state)

    def _rules(self, sum_neighbors: np.array) -> np.array:
        next_state = np.zeros_like(self.state, dtype=bool)
        alives = self.state == True
        two_three_neig = (sum_neighbors == 2) | (sum_neighbors == 3)
        three_neig = sum_neighbors == 3
        next_state[alives & two_three_neig] = True  # Rule 1
        next_state[~alives & three_neig] = True  # Rule 2
        return next_state

    def update(self):
        sum_neighbors = signal.convolve2d(self.state, self._kernel, mode="same")
        self.state = self._rules(sum_neighbors)
        self.generations += 1
        self.current_population = np.sum(self.state)
        return self.state
