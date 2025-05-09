#
# EscGridEnv.py
#   Author: Bill Xia
#   Created: 9/9/2024
#
# Purpose: Defines a simple environment that can be customized for the
#          EscapeWorld puzzle task.
#

# MiniGrid Imports.
from minigrid.minigrid_env import MiniGridEnv
from minigrid.core.mission import MissionSpace
from minigrid.core.grid import Grid
from minigrid.core.world_object import Goal, Wall
from minigrid.core.constants import TILE_PIXELS

# New Stuff.
from minigrid.core.NewObjects import (
    Crate,
    Button,
    ButtonDoor,
    PuzzleKey,
    PuzzleKeyDoor,
    FalseWall
)
from typing import Any, SupportsFloat

# Other.
from gymnasium.core import ActType, ObsType
from gymnasium import spaces
from numpy import array
from random import randint

class EscGridEnv(MiniGridEnv):
    '''
    Inherits from `MiniGridEnv`.

    Environments use array indexing, so any coordinates used by this class
    treat the top left corner of the environment as (0,0).
    '''

    def __init__(
        self,
        width=22,
        height=22,
        agent_start_pos=(5, 8),
        agent_start_dir=0,
        max_steps: int = 1000,
        grid_layout=None,
        use_rand_start=False,
        rand_objs: list[str] = [],
        **kwargs,
    ):

        # Defining starting position and direction for agents created in the
        # environment.
        self.agent_start_pos = agent_start_pos
        self.agent_start_dir = agent_start_dir

        # Storing starting layout.
        self.layout = grid_layout

        # Creating a list for storing all our buttons.
        self.button_list = []

        # Boolean for determining if the agent is holding a key.
        self.carrying = None

        # Defining the MissionSpace, which defines the set of possible missions
        # or tasks that an agent can be assigned in the environment.
        mission_space = MissionSpace(mission_func=self._gen_mission)

        # # I believe this limits the total number of steps we can take before
        # # we fail the mission.
        # if max_steps is None:
        #     max_steps = 4 * size**2

        super().__init__(
            mission_space=mission_space,
            width=width,
            height=height,
            max_steps=max_steps,
            see_through_walls=True,
            **kwargs,
        )

        # Observations are dictionaries containing an
        # encoding of the grid and a textual 'mission' string
        image_observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(self.agent_view_size, self.agent_view_size, 3),
            dtype="uint8",
        )
        self.observation_space = spaces.Dict(
            {
                "image": image_observation_space,
                "direction": spaces.Discrete(4),
                "mission": mission_space,
            }
        )

        # Constrain action space to just turning and moving.
        self.action_space = spaces.Discrete(3)

        # Save random start variable.
        self.use_rand_start = use_rand_start

        # Save objects that need to be randomly placed.
        self.rand_objs = rand_objs

    @staticmethod
    def _gen_mission():
        '''
        Returns a string defining a mission description.

        In the future, the string returned by this function will be more
        complex, and possibly not hardcoded.
        '''
        return "Reach the Goal"

    def _gen_grid(self, width, height):
        '''
        Overrides the function of the same name from the superclass. This
        method lets use generate a new grid-world.

        `width` and `height` define the dimensions of the environment.
        '''

        # Create an empty grid
        self.grid = Grid(width, height)

        # If no layout provided, use default.
        if self.layout == None:
            # Generate outer "wall".
            for i in range(5, 17):
                self.grid.set(3, i, FalseWall())
            for i in range(5, 17):
                if i != 9:
                    self.grid.set(18, i, FalseWall())
            for i in range(3, 19):
                self.grid.set(i, 5, FalseWall())
            for i in range(3, 19):
                self.grid.set(i, 16, FalseWall())

            # Place a goal square.
            self.put_obj(Goal(), 19, 9)


            ## TEST STUFF BELOW ## --------------------------------------------

            self.put_obj(Crate(), 9, 8)
            self.place_button(Button(), 11, 8)
            self.put_obj(ButtonDoor(), 17, 9)
            self.put_obj(PuzzleKey(), 15, 9)
            self.put_obj(PuzzleKeyDoor(), 18, 9)

            ## TEST STUFF ABOVE ## --------------------------------------------


        # Case for filling the grid with a string matrix.
        else:
            for j in range(0, height):
                for i in range(0, width):
                    # Layout is indexed by y before x.
                    cellStr = self.layout[j][i]
                    # Place object.
                    self.place_objStr(cellStr, (i, j))

        # Place random objects.
        for objStr in self.rand_objs:
            # self.place_objStr(objStr)
            y_coord = randint(6, 15)
            self.place_objStr(objStr, (19, y_coord))

        # Place the agent
        if self.agent_start_pos is not None and not self.use_rand_start:
            self.agent_pos = self.agent_start_pos
            self.agent_dir = self.agent_start_dir
        else:
            # If no start position is given, use this superclass method to
            # place the agent in a random spot in the environment.
            self.place_agent()


        self.mission = "Escape Grid"

    def step(
        self, action: ActType
    ) -> tuple[ObsType, SupportsFloat, bool, bool, dict[str, Any]]:
        self.step_count += 1

        reward     = 0
        terminated = False
        truncated  = False

        # Rotate left
        if action == self.actions.left:
            self.agent_dir -= 1
            if self.agent_dir < 0:
                self.agent_dir += 4

        # Rotate right
        elif action == self.actions.right:
            self.agent_dir = (self.agent_dir + 1) % 4

        # Move forward
        elif action == self.actions.forward:

            # Get the position in front of the agent
            fwd_pos = self.front_pos

            # Get the contents of the cell in front of the agent
            try:
                fwd_cell = self.grid.get(*fwd_pos)
            except:
                # Prevents the agent from leaving the environment.
                obs = self.gen_obs()
                return obs, reward, terminated, truncated, {}

            # Crate code.
            if isinstance(fwd_cell, Crate):
                # If the cell contains a crate, try to push it.
                push_dir = self.dir_vec
                if fwd_cell.push(self, fwd_pos, push_dir):
                    # If push was successful, move the agent forward.
                    self.agent_pos = fwd_pos
                    new_crate_pos = (
                        fwd_pos[0] + push_dir[0], 
                        fwd_pos[1] + push_dir[1]
                    )
                    cell_under_crate = fwd_cell.underneath
                    cell_behind_crate = fwd_cell.behind
                    # Logic to handle buttons. -------------------------------\
                    if isinstance(cell_under_crate, Button):
                        cell_under_crate.toggle(self, new_crate_pos)
                        self.update_doors()
                    if isinstance(cell_behind_crate, Button):
                        # print('MOVED OFF BUTTON')
                        cell_behind_crate.toggle(self, None)
                        self.update_doors()
                    # --------------------------------------------------------/
                    # Logic to handle goal. ----------------------------------\
                    if isinstance(cell_behind_crate, Goal):
                        terminated = True
                        # reward = self._reward()
                    # --------------------------------------------------------/

            # Key code.
            elif isinstance(fwd_cell, PuzzleKey):
                # If the agent isn't carrying a key...
                if self.carrying is None:
                    # Pick up the key.
                    self.carrying = fwd_cell
                    self.carrying.cur_pos = array([-1, -1])
                    self.grid.set(fwd_pos[0], fwd_pos[1], None)
                    self.agent_pos = fwd_pos
                    # Change the agent's color to indicate new status.
                    # print('Turned purple')
                    self.grid.make_agent_not_red()

            # KeyDoor code.
            elif isinstance(fwd_cell, PuzzleKeyDoor):
                # If the agent is carrying a key...
                if isinstance(self.carrying, PuzzleKey):
                    self.grid.set(fwd_pos[0], fwd_pos[1], None)
                    self.agent_pos = fwd_pos
                    self.carrying = None
                    self.grid.make_agent_red()

            # Base code.
            if fwd_cell is None or fwd_cell.can_overlap():
                self.agent_pos = tuple(fwd_pos)
            if fwd_cell is not None and fwd_cell.type == "goal":
                terminated = True
                # reward = self._reward()

        # Done action (not used by default)
        elif action == self.actions.done:
            pass

        else:
            raise ValueError(f"Unknown action: {action}")

        if self.step_count >= self.max_steps:
            truncated = True

        # We want to re-render the entire grid every step.
        if self.render_mode == "human":
            # print('\noccurs?')
            # self.render()
            self.grid.render(
                TILE_PIXELS,
                self.agent_pos,
                self.agent_dir
            )

        obs    = self.gen_obs()
        reward = self._reward(terminated, truncated)

        # print(obs['image'].shape)

        return obs, reward, terminated, truncated, {}

    def place_objStr(self, objStr: str, coords: tuple[int]=None):
        # Figure out the object to place.
        if objStr == 'w':
            obj = Wall()
        elif objStr == 'g':
            obj = Goal()
        elif objStr == 'c':
            obj = Crate()
        elif objStr == 'p':
            obj = Button()
            self.button_list.append(obj)
        elif objStr == 'd':
            obj = ButtonDoor()
        elif objStr == 'k':
            obj = PuzzleKey()
        elif objStr == 't':
            obj = PuzzleKeyDoor()
        elif objStr == 'f':
            obj = FalseWall()
        elif objStr == '':
            obj = None
        else:
            raise ValueError(f'Unrecognized cell code: {objStr}')

        # Place the object.
        if coords is None:
            # Do random placement.
            self.place_obj(obj)
        elif obj is None:
            pass
        else:
            # Do fixed placement.
            x, y = coords
            self.put_obj(obj, x, y)

    def place_button(self, button, x, y):
        self.put_obj(button, x, y)
        self.button_list.append(button)


    def update_doors(self):
        # Count the number of activated plates
        activated_plates = 0
        total_plates = 0
        for b in self.button_list:
            if b.is_activated:
                activated_plates += 1
            total_plates += 1

        # Update all PlateDoors based on the number of activated plates
        for obj in self.grid.grid:
            if isinstance(obj, ButtonDoor):
                if activated_plates == total_plates:
                    obj.open_door()
                else:
                    obj.close_door()

    def _reward(
        self,
        terminated: bool,   # Did the agent reach its Goal?
        truncated: bool,    # Did the agent exceed the maximum step count?
    ) -> float:
        '''
        Basic reward function.
        '''
        if terminated:
            return 1 - 0.99 * (self.step_count / self.max_steps)
        else:
            # print(env_encoder.encode_env(self))
            return 0



