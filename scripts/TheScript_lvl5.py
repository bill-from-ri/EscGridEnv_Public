#
# TheScript_lvl5.py
#   Author: Bill Xia
#   Created: 4/27/2025
#
# Purpose: Script for running lvl5 variant experiments.
#

# Imports.
from agent.Solver import Solver
import yaml

from EscGridEnv.EscGridEnv import EscGridEnv
from EscGridEnv.levels import (
    lvl_1, lvl_5, lvl_5b, lvl_5c, lvl_5d, lvl_5e
)
from minigrid.wrappers import ImgObsWrapper, FullyObsWrapper

from json import dump, load
from tqdm import tqdm
from os import listdir

# Globals.  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

LEVELS = {
    'lvl_5'  : lvl_5,
    'lvl_5b' : lvl_5b,
    'lvl_5c' : lvl_5c,
    'lvl_5d' : lvl_5d,
    'lvl_5e' : lvl_5e,
}

# Functions. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def combos(fn='agent/lvl5_config.yaml'):
    with open(fn) as f:
        data = yaml.full_load(f)
    combos = []
    for model in data.get('model'):
        for pm in data.get('prompt_method'):
            for exp in [1, 2]:
                for lvl_name in LEVELS.keys():
                    combos.append({
                        'model'  : model,
                        'prompt' : pm,
                        'exp'    : exp,
                        'lvl'    : lvl_name
                    })
    return combos

def run_experiment(combos):
    results = []
    curr_id = 0
    for c in tqdm(combos):
        for i in range(20):

            tag = f"{c['model']}_exp{c['exp']}_{c['prompt']}_{c['lvl']}_{i}"
            if f"{tag}.json" in listdir('data/lvl5_exps/backups'):
                continue

            agent = Solver(
                model_name=c['model'],
                experiment_num=c['exp'],
                plan_act_split=False,
                prompt_method=c['prompt'],
                encoding_meth='text'
            )

            # Set up env. - - - - - - - - - - - - - - - #
            env = EscGridEnv(                           #
                grid_layout=LEVELS[c['lvl']](),         #
                highlight=False                         #
            )                                           #
            env = FullyObsWrapper(env)                  #
            env = ImgObsWrapper(env)                    #
            env.unwrapped.render_mode = 'rgb_array'     #
            env.reset()                                 #
            # - - - - - - - - - - - - - - - - - - - - - #

            agent.reset_thinker()

            stats         = {}
            stats['id']   = curr_id
            stats         = agent.solve(env, c['lvl'])
            stats['lvl']  = c['lvl']
            stats['iter'] = i
            stats['meta'] = c

            curr_id += 1

            with open(f'lvl5_exps/backups/{tag}.json', 'w') as fp:
                dump(stats, fp, indent=4)

            results.append(stats)
    return results

def fill_results():
    rest_of_results = []
    for fn in listdir('lvl5_exps/backups'):
        with open(f"lvl5_exps/backups/{fn}") as fp:
            curr_data = load(fp)
        rest_of_results.append(curr_data)
    return rest_of_results

# Main. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():
    results = run_experiment(
        combos()
    )

    results += fill_results()

    with open('lvl5_exps/lvl5_exp_results.json', 'w') as fp:
        dump(results, fp, indent=4)

if __name__ == '__main__':
    main()