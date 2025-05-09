#
# TheScript.py
#   Author: Bill Xia
#   Created: 3/3/2025
#
# Purpose: Script for running our experiments.
#

# Imports.
from agent.Solver import Solver
import yaml

from EscGridEnv.EscGridEnv import EscGridEnv
from EscGridEnv.levels import (
    lvl_1, lvl_3, lvl_5, lvl_9, lvl_11, lvl_12
)
from minigrid.wrappers import ImgObsWrapper, FullyObsWrapper

from json import dump
from os import listdir

# Globals.  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

LEVELS = {
    'lvl_1' : lvl_1,
    'lvl_3' : lvl_3,
    'lvl_5' : lvl_5,
    'lvl_9' : lvl_9,
    'lvl_11': lvl_11,
    'lvl_12': lvl_12
}

# Main. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():

    mode = int(input("Which mode is this (1, 2)? "))

    with open('agent/config.yaml', 'r') as f:
        data = yaml.full_load(f)

    # Get argument combinations.
    combos = []
    for model in data.get('model'):
        for do_split in data.get('do_split'):
            for pm in data.get('prompt_method'):
                for encoding in data.get('encoding'):
                    combos.append((model, do_split, pm, encoding))

    for number in range(3):
        for c in combos:

            if f'iter{number}_{c[0]}_split={c[1]}_encoding={c[3]}.json' in listdir(f'data/raw/exp{mode}/{c[2]}'):
                continue
            else:
                print(listdir(f'data/raw/exp{mode}/{c[2]}'))

            print(f"\nNow working on iter{number}_{c[0]}_split={c[1]}_encoding={c[3]}.json\n")

            agent = Solver(
                model_name=c[0],
                experiment_num=mode,
                plan_act_split=c[1],
                prompt_method=c[2],
                encoding_meth=c[3]
            )

            stats_list = []
            for lvl_str, lvl in LEVELS.items():
                # Set up env. - - - - - - - - - - - - - - - #
                env = EscGridEnv(                           #
                    grid_layout=lvl(),                      #
                    highlight=False                         #
                )                                           #
                env = FullyObsWrapper(env)                  #
                env = ImgObsWrapper(env)                    #
                env.unwrapped.render_mode = 'rgb_array'     #
                env.reset()                                 #
                # - - - - - - - - - - - - - - - - - - - - - #

                agent.reset_thinker()

                stats = {}
                stats = agent.solve(env, lvl_str)
                stats['lvl'] = lvl_str

                stats_list.append(stats)
                print(f"  Finished {lvl_str}")

            with open(f'data/raw/exp{mode}/{c[2]}/iter{number}_{c[0]}_split={c[1]}_encoding={c[3]}.json', 'w') as fp:
                dump(stats_list, fp, indent=4)
            print("  Finished with a MODEL\n")


if __name__ == '__main__':
    main()



