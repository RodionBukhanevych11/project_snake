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
        self.config = config
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
        self.snake_size = config["snake_size"]
        # Init a numpy matrix with zeros of predefined size
        self.size = size
        self.world = np.zeros(size)
        # Fill in the indexes gaps to add walls to the grid world
        self.world[0, :] = self.wall
        self.world[:, 0] = self.wall
        self.world[:, -1] = self.wall
        self.world[-1, :] = self.wall 
        # Get available positions for placing food (choose all positions where world block = 0)
        self.available_food_positions = list(zip(*np.where(self.world == 0)))
        # Init snake
        self.snake = self.init_snake()
        # Set food
        self.init_food()

    def init_snake(self):
        """
        Initialize a snake
        """
        # choose a random position between [SNAKE_SIZE and SIZE - SNAKE_SIZE]
        start_position = random.randint(self.snake_size, self.size[0] - self.snake), \
                         random.randint(self.snake_size, self.size[0] - self.snake)
        # choose a random direction index
        start_direction_index = random.randint(0,3)
        new_snake = Snake(start_position, start_direction_index, self.config)

        return new_snake

    def init_food(self):
        """
        Initialize a peace of food
        """
        # Update available positions for food placement considering snake location
        available_food_positions = list(zip(*np.where(self.world == 0)))
        chosen_position = random.sample(available_food_positions,1)
        # init new food
        self.food_position = chosen_position
        self.world[chosen_position] = self.food

    def get_observation(self):
        """
        Get observation of current world state
        """
        obs = self.world.copy()
        snake = self.snake if self.snake.alive else None
        if snake:
            for block in snake.blocks:
                obs[block] = self.snake.snake_block
            # snakes head
        return obs

    def move_snake(self, action):
        """
        Action executing
        """
        # define reward variable
        reward = 0
        # food needed flag
        new_food_needed = False
        # check if snake is alive
        if self.snake.alive:
            # perform a step (from Snake class)
            new_snake_head, old_snake_tail = self.snake.step(action=action)
            # Check if snake is outside bounds
            if (new_snake_head[0] <= 0 or new_snake_head[0] >= self.world.shape[0]) or \
                (new_snake_head[1] <= 0 or new_snake_head[1] >= self.world.shape[1]):
                self.snake.alive = False
            # Check if snake eats itself
            elif new_snake_head in self.snake.blocks[1:]:
                self.snake.alive = False
            #  Check if snake eats the food
            if new_snake_head == self.food_position:
                # Remove old food
                self.food_position = None
                # Add tail again
                self.snake.blocks = self.snake.blocks.append(old_snake_tail)
                # Request to place new food
                new_food_needed = True
                # update reward
                reward = self.eat_reward
            elif self.snake.alive:
                # Didn't eat anything, move reward
                reward = self.move_reward
        # Compute done flag and assign dead reward
        done = not self.snake.alive
        reward = reward if self.snake.alive else self.dead_reward
        # Adding new food
        if new_food_needed:
            self.init_food()

        return reward, done, self.snake.blocks