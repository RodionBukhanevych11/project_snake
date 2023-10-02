import random
import numpy as np
from src.modules.env.core.snake import Snake


class World:
    def __init__(self, size, start_position, start_direction_index, food_position, config):
        """
        @param size: tuple
        @param custom: bool
        @param start_position: tuple
        @param start_direction_index: int
        @param food_position: tuple
        """
        # for custom init
        self.start_position = start_position
        self.start_direction_index = start_direction_index
        self.food_position = food_position
        # rewards
        self.dead_reward = config["dead_reward"]
        self.move_reward = config["move_reward"]
        self.eat_reward = config["eat_reward"]
        self.food = config["food_block"]
        self.wall = config["wall"]
        self.directions = config["directions"]
        # Init a numpy matrix with zeros of predefined size
        self.size = size
        self.world = np.zeros(size)
        # Fill in the indexes gaps to add walls to the grid world
        self.world[0,:] = self.wall
        ...
        ...
        ...
        ...
        # Get available positions for placing food (choose all positions where world block = 0)
        self.available_food_positions = ...
        # Init snake
        self.snake = self.init_snake()
        # Set food
        self.init_food()

    def init_snake(self):
        """
        Initialize a snake
        """
        # choose a random position between [SNAKE_SIZE and SIZE - SNAKE_SIZE]
        start_position = ...
        # choose a random direction index
        start_direction_index = ...
        new_snake = ...

        return new_snake

    def init_food(self):
        """
        Initialize a peace of food
        """
        snake = self.snake if self.snake.alive else None
        # Update available positions for food placement considering snake location
        available_food_positions = ...
        chosen_position = random.sample(available_food_positions,1)
        # init new food
        self.world[..., ...] = self.FOOD

    def get_observation(self):
        """
        Get observation of current world state
        """
        obs = self.world.copy()
        snake = self.snake if self.snake.alive else None
        if snake:
            for block in snake.blocks:
                obs[..., ...] = ...
            # snakes head
            obs[..., ...] = ...
        return obs

    def move_snake(self, action):
        """
        Action executing
        """
        # define reward variable
        reward = ...
        # food needed flag
        new_food_needed = ...
        # check if snake is alive
        if self.snake.alive:
            # perform a step (from Snake class)
            new_snake_head, old_snake_tail = ...
            # Check if snake is outside bounds
            if ...:
                self.snake.alive = ...
            # Check if snake eats itself
            elif ...:
                self.snake.alive = ...
            #  Check if snake eats the food
            if ...:
                # Remove old food
                self.food_position = ...
                # Add tail again
                self.snake.blocks = ...
                # Request to place new food
                new_food_needed = ...
                # update reward
                reward = ...
            elif self.snake.alive:
                # Didn't eat anything, move reward
                reward = ...
        # Compute done flag and assign dead reward
        done = not ...
        reward = reward if self.snake.alive else self.dead_reward
        # Adding new food
        if new_food_needed:
            ...

        return reward, done, self.snake.blocks