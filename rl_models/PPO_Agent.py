#
# PPO_agent.py
# Bill Xia
# 10/14/24
#
# Purpose: Contains the PPO_Agent class, which defines a Proximal Policy
#          Optimization Agent for navigating a MiniGrid environment.
#

# Imports
import torch
import torch.nn as nn
from gymnasium import spaces
from stable_baselines3 import PPO
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor

import numpy as np

# Helper Class.
class MinigridFeaturesExtractor(BaseFeaturesExtractor):
    '''
    The feature extractor takes in an observation space and converts it into a
    form that can be used to train a neural network.
    '''

    def __init__(self, observation_space: spaces.Box,
                        features_dim: int = 512,
                        normalized_image: bool = False) -> None:

        super().__init__(observation_space, features_dim)
        n_input_channels = observation_space.shape[0]
        self.cnn = nn.Sequential(
            nn.Conv2d(n_input_channels, 16, (2, 2)),
            nn.ReLU(),
            nn.Conv2d(16, 32, (2, 2)),
            nn.ReLU(),
            nn.Conv2d(32, 64, (2, 2)),
            nn.ReLU(),
            nn.Flatten(),
        )

        # Compute shape by doing one forward pass
        with torch.no_grad():
            n_flatten = self.cnn(torch.as_tensor(observation_space.sample()[None]).float()).shape[1]

        self.linear = nn.Sequential(nn.Linear(n_flatten, features_dim), nn.ReLU())

    def forward(self, observations: torch.Tensor) -> torch.Tensor:
        '''
        I'M PRETTY SURE THIS FUNCTION WORKS.
        '''
        return self.linear(self.cnn(observations))

# Class
class PPO_Agent:

    def __init__(self, env,                 # The environment.
                       features_dim=128,    # Size of PPO NN input.
                       episodes=2e5,        # Number of training time steps.
                       dev=None,            # Hopefully a GPU.
                       verbose=0            # Verbose training?
                ):

        # Define hyperparameter.
        self.episodes = episodes

        # Initialize the model policy kwargs, then the model itself.
        policy_kwargs = dict(
            features_extractor_class=MinigridFeaturesExtractor,
            features_extractor_kwargs=dict(features_dim=features_dim),
        )
        self.model = PPO(
            'CnnPolicy',
            env,
            policy_kwargs=policy_kwargs,
            device=dev if dev is not None else 'auto',
            verbose=verbose
        )

    # Training function.
    def train(self, progress_bar=False):
        self.model.learn(
            self.episodes,
            progress_bar=progress_bar
        )

    def predict(self, obs):
        '''
        Chooses an action given a observation. This function is for
        prediction, not training, so we always choose the optimal action.
        '''
        action, _ = self.model.predict(obs, deterministic=False)
        return action

    # Functions for saving and loading the model. - - - - - - - - - - - - - - -
    def save_model(self, fname):
        self.model.save(fname)

    def delete_model(self):
        del self.model

    def load_model(self, fname):
        self.model = PPO.load(fname)

    def set_parameters(self, param_dict):
        self.model.set_parameters(param_dict)

    def get_parameters(self):
        return self.model.get_parameters()