import numpy as np
from typing import Tuple


class Snake:
    def __init__(self, head_position, direction_index, config):
        """@param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = config["snake_block"]
        self.snake_length = ...
        self.directions = ...
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = ...
        # Place the snake
        self.blocks = ...
        current_position = np.array(head_position)
        for i in range(1, self.snake_length):
            # Direction inverse of moving
            current_position = current_position - ...
            self.blocks.append(tuple(current_position))

    def step(self, action) -> Tuple[Tuple, Tuple]:
        # Execute one-time step within the environment
        """
               @param action: int
               @param return: tuple, tuple
               """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        ...
        # Remove tail
        tail = ...
        # Check new head
        ...
        # Add new head
        new_head = ...
        return new_head, tail