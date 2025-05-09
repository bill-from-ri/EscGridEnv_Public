#
# Prompt.py
#   Author: Bill Xia
#   Created: 2/3/2025
#
# Purpose: Module to handle LLM prompts.
#

# Imports.
import ollama

# Functions. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_prompt_msg(prompt_name, **kwargs):
    '''
    Generates the initial prompt for functions in the Thinking module.

    Args:
        prompt_name (str): The name of the prompt of interest.
        **kwargs: Arguments specific to the prompt of interest.

    Returns:
        str: The initial prompt of interest.
    '''

    # No affordances; basic prompting.
    if prompt_name == 'solution_plan_exp_1_base':
        return ' '.join([
            "[Prompt]",
            "You are a planner for an agent in a 2D GridWorld environment. You",
            "are given an observation of the environment.",
            "You are also given a goal that the agent must achieve.",

            "Your task is to generate a high-level plan that the agent can",
            "follow to achieve its goal. Then, generate a low-level action",
            "sequence that the agent can execute to achieve its goal.",

            "\n[Observation]",
            kwargs['obs'],
            "\n[Goal]",
            "The agent must move to the same cell as the Goal object.",
            "\n[Plan]\n"
        ])

    # No affordances; CoT prompting.
    elif prompt_name == 'solution_plan_exp_1_cot':
        return ' '.join([
            "[Prompt]",
            "You are a planner for an agent in a 2D GridWorld environment.",
            "You are given an observation of the environment.",
            "You are also given a goal that the agent must achieve.",

            "Your task is to generate a high-level plan that the agent can",
            "follow to achieve its goal. Then, generate a low-level action",
            "sequence that the agent can execute to achieve its goal.",
            "Below is an example observation, goal and plan. Use the example,",
            "as a reference for your own problem solving steps."

            "\n[EXAMPLE]"

            "\n[Observation]",
            "The agent is located at (5, 8). A green object is located at",
            "(19, 13). A brown border forms an enclosure around the agent as",
            "well as all objects except the green object, and the green object",
            "at (19, 13) There is an opening in the enclosure at (18, 13).",

            "\n[Goal]",
            "The agent must move to the same cell as the Goal object.",

            "\n[Plan] First determine that the green object is the Goal object.",
            "Align the agent on the horizontal axis (y=13) by moving DOWN.",
            "Because the agent is at y=8, it must move DOWN 13 - 8 = 5 times.",
            "Next, move the agent to reach the goal (x=19) by moving RIGHT.",
            "Because the agent is at x=5, it must move RIGHT 19 - 5 = 14 times.\n",
            "[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]",

            "\n[ACTUAL]"

            "\n[Observation]",
            kwargs['obs'],
            "\n[Goal]",
            "The agent must move to the same cell as the Goal object.",
            "\n[Plan] "
        ])

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # Affordances; basic prompting.
    elif prompt_name == 'solution_plan_exp_2_base':
        return ' '.join([
            "[Prompt]",
            "You are a planner for an agent in a 2D GridWorld environment. You",
            "are given an observation of the environment.",
            "You are also given a goal that the agent must achieve.",
            "You are also given a set of object affordances for objects in",
            "the environment.",

            "Your task is to generate a high-level plan that the agent can",
            "follow to achieve its goal. Then, generate a low-level action",
            "sequence that the agent can execute to achieve its goal.",

            "\n[Observation]",
            kwargs['obs'],
            "\n[Goal]",
            "The agent must move to the same cell as the Goal object.",
            "\n[Object Affordances]",
            "\n".join([f"{k} : {v}" for k, v in kwargs['affs'].items()]),
            "\n[Plan]\n"
        ])

    # Affordances; CoT prompting.
    elif prompt_name == 'solution_plan_exp_2_cot':
        return ' '.join([
            "[Prompt]",
            "You are a planner for an agent in a 2D GridWorld environment. You",
            "are given an observation of the environment.",
            "You are also given a goal that the agent must achieve.",
            "You are also given a set of object affordances for objects in",
            "the environment.",

            "Your task is to generate a high-level plan that the agent can",
            "follow to achieve its goal. Then, generate a low-level action",
            "sequence that the agent can execute to achieve its goal.",
            "Below is an example observation, goal and plan. Use the example,",
            "as a reference for your own problem solving steps."

            "\n[EXAMPLE]",

            "\n[Observation]",
            "The agent is located at (5, 8). A green object is located at",
            "(19, 13). A brown border forms an enclosure around the agent as",
            "well as all objects except the green object, and the green object",
            "at (19, 13) There is an opening in the enclosure at (18, 13).",

            "\n[Goal]",
            "The agent must move to the same cell as the Goal object.",

            "\n[Object Affordances]",
            "\n".join([f"{k} : {v}" for k, v in kwargs['affs'].items()]),

            "\n[Plan] First determine that the green object is the Goal object.",
            "Align the agent on the horizontal axis (y=13) by moving DOWN.",
            "Because the agent is at y=8, it must move DOWN 13 - 8 = 5 times.",
            "Next, move the agent to reach the goal (x=19) by moving RIGHT.",
            "Because the agent is at x=5, it must move RIGHT 19 - 5 = 14 times.\n",
            "[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]",

            "\n[ACTUAL]",

            "\n[Observation]",
            kwargs['obs'],
            "\n[Goal]",
            "The agent must move to the same cell as the Goal object.",
            "\n[Object Affordances]",
            "\n".join([f"{k} : {v}" for k, v in kwargs['affs'].items()]),
            "\n[Plan] "
        ])

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    elif prompt_name == 'initialization':
        return ' '.join([
            "An agent wants to reach a Goal in a 2D GridWorld environment.\n",
            "[Action Space] There exist four possible actions that the",
            "agent can take: 0, move RIGHT one space; 1, move DOWN one",
            "space; 2, move LEFT one space; 3, move UP one space.",
        ])

def prompt(model_name, **kwargs):
    '''
    Prompts the desired LLM with a set of kwargs.

    Args:
        model_name (str): The name of the LLM.
        **kwargs: Arguments specfic to the LLM being prompted.

    Returns:
        dict: A dictionary containing values desired by the Thinking module.
    '''

    if model_name == 'llama3':
        model = 'llama3:70b'
    elif model_name == 'qwen':
        model = 'qwen2.5:14b'
    elif model_name == 'deepseek':
        model = 'deepseek-r1:8b'

    if kwargs['response_format'] is not None:

        response = ollama.chat(
            model=model,
            messages=kwargs['messages'],
            format=kwargs['response_format'].model_json_schema()
        )

        try:
            results = kwargs['response_format'].model_validate_json(response.message.content).model_dump()
        except:
            # Create generic output.
            results = {
                'hypotheses'          : {},
                'plan'                : '',
                'actionSeq'           : [],
                'hypothesis_was_true' : False,
                'updated_affordance'  : ''
            }

    else:

        response = ollama.chat(
            model=model,
            messages=kwargs['messages']
        )

        results = response.message.content

    return results



