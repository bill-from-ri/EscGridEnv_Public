#
# Thinker.py
#   Author: Bill Xia
#   Created: 3/26/2025
#
# Purpose: Module for the thinking portion of our architecture. It uses an LLM
#          to solve an EscGridEnv puzzle either with or without NLWMs.
#

# Imports.
import agent.Prompt as Prompt
from pydantic import BaseModel
from nltk.tokenize import word_tokenize

# Helper Classes for Structured Outputs.
class ActionPlan(BaseModel):
    plan: str
    actionSeq: list[int]

# Class.
class Thinker:

    def __init__(
            self,
            client_name,
            plan_act_split,
            prompt_method
    ):
        self.client_name    = client_name
        self.plan_act_split = plan_act_split
        self.prompt_method  = prompt_method

        self.chat_history = [
            {'role': 'system',
             'content': Prompt.get_prompt_msg('initialization')}
        ]

    def update_prompt(self, role, content):
        self.chat_history.append(
            {'role'   : role,
             'content': content}
        )

    def reset_prompt(self):
        self.chat_history  = [
            {'role': 'system',
             'content': Prompt.get_prompt_msg('initialization')}
        ]

    def get_chat_hist_size(self):
        '''
        Returns the number of tokens in the chat history. Includes system,
        user, and assisstant messages.
        '''
        t_count = 0
        for msg in self.chat_history:
            if msg['content'] is None:
                continue
            else:
                print(msg['content'])
                t_count += len(word_tokenize(str(msg['content'])))
        return t_count

    def solve(self, hypotheses, obs, **kwargs):
        '''
        Given a dictionary of affordances, an LLM tries to solve the current level.

        Args:
            hypotheses (dict[str, str]): A dictionary of object affordances.

            obs (str): A representation of an observation made in the environment.

        Returns:
            (str, list[int], int): A rationale and a list of action instructions
                for the agent to execute.
        '''

        # Initialize starting prompt.
        prompt_name = '_'.join([
            'solution_plan',
            f'exp_{kwargs["exp_num"]}',
            self.prompt_method
        ])
        # Possible Prompt Names:
        #   solution_plan_exp_1_base
        #   solution_plan_exp_1_cot
        #   solution_plan_exp_2_base
        #   solution_plan_exp_2_cot
        init_prompt = Prompt.get_prompt_msg(
            prompt_name,
            obs=obs,
            affs=hypotheses,
        )

        # Creating actual prompt.
        self.update_prompt('user', init_prompt)

        # Prompting.
        if self.plan_act_split == False:
            completion = Prompt.prompt(
                self.client_name,
                messages=self.chat_history,
                response_format=ActionPlan
            )
            self.update_prompt(
                'assistant',
                '\n'.join([f"{k} : {v}" for k, v in completion.items()])
            )

            plan = completion['plan']
            seq  = completion['actionSeq']

        return (plan, seq)



