import numpy as np
import typer

from conways_game_of_life.controller import GameController
from conways_game_of_life.model import GameLife
from conways_game_of_life.view import Interface

# Initialize Typer CLI
cli = typer.Typer(add_completion=False)


@cli.command()
def conways(
    save_gif: bool = typer.Option(False, help="Save gif after closing animation."),
    initialize: bool = typer.Option(False, help="Select initial state by hand."),
):
    """
    Simulate Conway's Game of Life.
    """
    # Determine if we use a random initial state or a user-defined initial state
    random_state = not initialize
    initial_state = (
        np.random.rand(100, 150) < 0.5
        if random_state
        else np.zeros((100, 150), dtype=bool)
    )

    # Set up the view, model, and controller
    view = Interface(initial_state)
    model = GameLife(initial_state)
    controller = GameController(model, view, save_gif)

    # Run the simulation based on initialization option
    if not random_state:
        controller.get_initial_state()
    else:
        controller.run()


if __name__ == "__main__":
    cli()
