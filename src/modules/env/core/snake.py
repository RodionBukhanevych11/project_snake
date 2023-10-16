import numpy as np
from typing import Tuple, List, Dict


class Snake:
    def __init__(self, head_position, direction_index, config):
        """@param head_position: tuple
        @param direction_index: int
        @param length: int
        """
        # Information snake need to know to make the move
        self.snake_block = config["snake_block"]
        self.snake_length = config["snake_length"]
        self.directions = config["movement_directions"]
        self.current_direction_index = direction_index
        # Alive identifier
        self.alive = True
        # Place the snake
        self.blocks = [head_position]
        current_position = np.array(head_position)
        for _ in range(1, self.snake_length):
            # Direction inverse of moving
            current_position = current_position - self.directions[direction_index]
            self.blocks.append(tuple(current_position))

    def step(self, action: int) -> tuple[Tuple, Tuple]:
        # Execute one-time step within the environment
        """
               @param action: int
               @param return: tuple, tuple
               """
        # Check if action can be performed (do nothing if in the same direction or opposite)
        if action != -self.current_direction_index:
            self.current_direction_index = action
        # Remove tail
        tail = self.blocks[-1]
        self.blocks = self.blocks[:-1]
        # Check new head
        new_head = np.array(self.blocks[0]) + np.array(self.directions[self.current_direction_index])
        # Add new head
        self.blocks = [new_head] + self.blocks
        return new_head, tail