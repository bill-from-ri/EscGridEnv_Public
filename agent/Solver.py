#
# Solver.py
#   Author: Bill Xia
#   Created: 3/26/2025
#
# Purpose: Module for the updated Solver, which is the driver module for our
#          LLM agent. This version is easier to customize according to the
#          parameters we defined on 3/26.
#

# Imports.
import agent.Perception as Perception
import agent.Thinker as Thinker
import agent.Action as Action
from agent.NLWMs import get_NLWMs

# Class
class Solver:
    '''
    New driver module for our LLM agent.
    '''

    def __init__(
            self,
            model_name,     # 'llama', 'deepseek', or 'qwen'
            experiment_num, #  1 or 2. Decides if affs will be used or not
            plan_act_split, #  bool; This parameter wasn't used in my experiments
            prompt_method,  # 'base', 'cot'
            encoding_meth,  # 'matrix', 'text'
    ):
        self.thinker        = Thinker.Thinker(model_name, plan_act_split, prompt_method)
        self.exp_num        = experiment_num
        if encoding_meth == 'matrix':
            self.obs_func = Perception.obs
        else:
            self.obs_func = Perception.obs_desc

    def reset_thinker(self):
        '''
        Resets the thinker while retaining the old affordances.
        '''
        self.thinker.reset_prompt()

    def solve(self, env, lvl):

        # Define Metrics to Capture.
        metrics                  = {}
        metrics['explore_steps'] = 0   # Steps used to test hypotheses
        metrics['exploit_steps'] = 0   # Steps used to solve
        metrics['tests']         = []  # Dicts with obj, hyp, and test
        metrics['all_hyps']      = []  # All newly-generated hypotheses
        metrics['bad_hyps']      = []  # New hyps rejected by verification
        metrics['final_hyps']    = {}  # New hyps that passed verification

        # Generate initial observation and hypothesis.
        obs = self.obs_func(env)
        hypotheses = {}
        if self.exp_num == 2:
            hypotheses = get_NLWMs(lvl)

        # Solve.
        env.reset()
        solve_plan, udlr = self.thinker.solve(
            hypotheses,
            obs,
            exp_num=self.exp_num
        )
        print('Generated Potential Solution')

        # Execute plan.
        solution = Action.udlr_to_lrf(udlr, env.unwrapped.agent_dir)
        done = False
        for action in solution:
            _, _, done, _, _ = env.step(action)
            metrics['exploit_steps'] += 1
            if done:
                break

        # Final metrics update.
        metrics['final_hyps']  = hypotheses
        metrics['completed']   = done
        metrics['solve_plan']  = solve_plan
        metrics['solution']    = solution
        metrics['tokens']      = self.thinker.get_chat_hist_size()
        metrics['total_steps'] = metrics['explore_steps'] + metrics['exploit_steps']

        return metrics



