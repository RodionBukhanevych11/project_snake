import gym
from gym import spaces
import numpy as np

from .core.world import World
from .utils.renderer import Renderer

'''
    Configurable single snake environment.
    Parameters:
        - OBSERVATION_MODE: return a raw observation (block ids) or RGB observation
        - OBS_ZOOM: zoom the observation (only for RGB mode, FIXME)
'''

class SnakeEnv(gym.Env):
    metadata = {
        'render': ['human', 'rgb_array'],
        'observation.types': ['raw', 'rgb']
    }

    def __init__(self, config, render_zoom=20, start_position=None, start_direction_index=None,
                 food_position=None):
        # for custom init
        self.start_position = start_position
        self.start_direction_index = start_direction_index
        self.food_position = food_position
        self.config = config
        #  Set size of the game world
        self.size = config["size"]
        # Create world
        self.world = self.create_world()
        # Init current step for future usage
        self.current_step = 0
        # Init alive flag
        self.alive = True
        # Observation space
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(self.SIZE[0], self.SIZE[1]),
                                            dtype=np.uint8)
        # Action space
        self.action_space = spaces.Discrete(len(self.world.directions))
        #  Set renderer
        self.render_zoom = render_zoom
        self.renderer = None

    def step(self, action):
        """
        Execute action
        @param action: int
        @return: np.array (observation after the action), int (reward), bool ('done' flag), np.array (snake)
        """
        # Check if game is ended
        #if not self.alive:
        # Perform the action
        reward, done, snake = self.world.move_snake(action=action)
        # Disable interactions if snake dead
        if not self.alive:
            self.action_space = None

        return self.world.get_observation(), reward, done, snake
    
    def create_world(self):
        return World(size=self.size,
                    start_position=self.start_position,
                    start_direction_index=self.start_direction_index,
                    food_position=self.food_position,
                    config=self.config)

    def reset(self):
        """
        Reset environment to the initial state
        @return: initial observationsssswda
        """
        # Reset step counters

        # Set 'alive' flag
        self.alive = False
        # Create world
        self.world = self.create_world()

        return self.world.get_observation()

    def render(self, mode='human', close=False):
        """
        Render environment depending on the mode
        @param mode: str
        @param close: bool
        @return: np.array
        """
        if not close:
            # Renderer lazy loading
            if self.renderer is None:
                self.renderer = Renderer(size=self.size, zoom_factor=self.render_zoom)
            return self.renderer.render(self.world.get_observation(), mode=mode, close=False)

        def close(self):
            """
            Close rendering
            """
            quit()

        if self.renderer:
            self.renderer.close()
            self.renderer = None