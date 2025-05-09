#
# Perception.py
#   Author: Bill Xia
#   Created: 1/21/2025
#
# Purpose: Module for converting observations from an EscGridEnv environment
#          into a string form that can be processed by an LLM.
#

# Imports.
from minigrid.core.NewObjects import FalseWall

# Helpers. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_agentPos(env) -> tuple[int, int]:
    '''
    Finds the coordinates of the agent in a MiniGrid environment.

    Args:
        env (MiniGridEnv): The MiniGrid environment instance

    Returns:
        coords (tuple[int, int]): Coordinates (x, y) of the agent.
    '''
    return env.unwrapped.agent_pos


def detect_gap(env) -> tuple[int, int]:
    '''
    Finds the gap in the wall in a MiniGrid environment.

    Args:
        env (MiniGridEnv): The MiniGrid environment instance

    Returns:
        coords (tuple[int, int]): Coordinates (x, y) of the gap.
    '''

    left_wall_x_coord = 18
    top_wall_y_coord  = 5
    for j in range(12):
        curr_cell_y_coord = top_wall_y_coord + j
        cell = env.unwrapped.grid.get(
            left_wall_x_coord,
            curr_cell_y_coord
        )
        if not isinstance(cell, FalseWall):
            return (left_wall_x_coord, curr_cell_y_coord)

    # If you find no gap...
    return None


# Functions. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def obs(env) -> list[str]:
    '''
    Generates a symbolic (matrix) representation of a MiniGrid environment.

    Args:
        env (MiniGridEnv): The MiniGrid environment instance.

    Returns:
        str: A symbolic representation of the environment.
    '''

    # Initialize encoding.
    encoding = [['' for _ in range(env.unwrapped.height)] for _ in range(env.unwrapped.width)]

    # Iterate through the Grid to get object locations.
    for i in range(env.unwrapped.height):
        for j in range(env.unwrapped.width):
            cell = env.unwrapped.grid.get(i, j)

            if cell is None:
                encoding[j][i] = ''

            # Not the cleanest way to differentiate buttondoors, but doing it
            # by type was causing a circular definition error.
            elif cell.color == 'blue':
                if cell.is_open:
                    encoding[j][i] = ''
                else:
                    encoding[j][i] = str(cell.color)

            else:
                encoding[j][i] = str(cell.color)

    # Get agent position.
    agentPos = get_agentPos(env)
    encoding[agentPos[1]][agentPos[0]] = 'agent'

    # Convert to string.
    encoding = '\n'.join([
        str(row) for row in encoding
    ])

    return encoding


def obs_desc(env) -> str:
    '''
    Generates a text description of a MiniGrid environment.

    Args:
        env (MiniGridEnv): The MiniGrid environment instance.

    Returns:
        str: A string description of the environment.
    '''

    agent_pos = f"The agent is located at {get_agentPos(env)}. "

    objects       = []
    out_of_bounds = []
    for i in range(env.unwrapped.height):
        for j in range(env.unwrapped.width):
            cell = env.unwrapped.grid.get(i, j)
            if cell is None:
                pass
            elif cell.color == 'blue' and cell.is_open:
                pass
            elif cell.color != 'brown':
                objects.append(f"A {cell.color} object is located at {(i, j)}.")
                if ((i < 3 or i > 18) or (j < 5 or j > 16) and cell.color != 'green'):
                    out_of_bounds.append((cell.color, (i, j)))

    # Figure out what's outside the enclosure.
    outsiders = [
        f"the {color} object at {coord},"
        for color, coord in out_of_bounds[:-1]
    ] + [f"and the {out_of_bounds[-1][0]} object at {out_of_bounds[-1][1]}"]
    outside = ' '.join(outsiders)

    desc = " ".join([
        "A brown border forms an enclosure around the agent as well as all",
        "objects except the green object,",
        outside
    ])

    gap_loc = detect_gap(env)
    if gap_loc is not None:
        desc += f" There is an opening in the enclosure at {gap_loc}."
    else:
        desc += f" There is no apparent opening in the enclosure."

    return agent_pos + " ".join(objects) + " " + desc



