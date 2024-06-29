
"""
Conway's Game of Life.

Script to simulate Conway's Game of Life.

Usage:
    conways [--initialize --save_gif]

Options: 
    --save_gif      Save gif after closing animation. [default: False]
    --initialize    Select initial state by hand. [default: False]
"""
import docopt
from .model import GameLife
from .view import Interface
from .controller import GameController
import numpy as np


def main():
    args = docopt.docopt(__doc__)
    save = args['--save_gif']
    random_state = not args['--initialize']
    initial_state = np.random.rand(100, 150) < 0.5 if random_state else np.zeros((100, 150), dtype=bool)
    
    view = Interface(initial_state)
    model = GameLife(initial_state)
    controller = GameController(model, view, save)
    
    if not random_state:
        controller.get_initial_state()
    else:
        controller.run()

if __name__ == "__main__":
    main()

