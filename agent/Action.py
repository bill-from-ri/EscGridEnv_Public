#
# Action.py
#   Author: Bill Xia
#   Created: 1/22/2025
#
# Purpose: Module for converting up-down-left-right actions into
#          left-right-forward actions. We need this module because LLMs are
#          more comfortable giving UDLR instructions than LRF instructions,
#          and MiniGrid only works with LRF instructions.
#

# Globals.
LEFT    = 0
RIGHT   = 1
FORWARD = 2

# Helpers. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def updateDir(
        direction: int,
        updateVal: int
) -> int:
    '''
    Updates the agent's direction for our loop down below.

    Args:
        direction (int)  : The agent's starting direction.
        updateVale (int) : How much we want to change the direction.

    Returns:
        The agent's new direction.
    '''

    direction += updateVal
    if direction < 0:
        direction += 4
    if direction > 3:
        direction -= 4

    return direction

# Functions. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def udlr_to_lrf(
        actionSeq: list[int],
        agentDir: int
) -> list[int]:
    '''
    Converts a UDLR action sequence into an LRF action sequence.

    Args:
        actionSeq (list[int]) : A UDLR action sequence.
        agentDir (int)        : The starting direction of the agent (usually
                                `env.unwrapped.agent_dir`).

    Returns:
        An LRF action sequence.
    '''

    if len(actionSeq) > 0:
        try:
            assert isinstance(actionSeq[0], int)
        except:
            print(f"Unrecognized action sequence: {actionSeq}")
            return []

    lrfSeq = []
    for action in actionSeq:

        # If the agent is facing the correct direction...
        if agentDir == action:

            # Move forward.
            lrfSeq.append(FORWARD)

        else:

            # Otherwise, rotate in the correct direction, then move foward.
            if action - agentDir == -1 or action - agentDir == 3:
                lrfSeq.append(LEFT)
                lrfSeq.append(FORWARD)
                agentDir = updateDir(agentDir, -1)
            elif action - agentDir == 1 or action - agentDir == -3:
                lrfSeq.append(RIGHT)
                lrfSeq.append(FORWARD)
                agentDir = updateDir(agentDir, 1)
            else:
                lrfSeq.append(RIGHT)
                lrfSeq.append(RIGHT)
                agentDir = updateDir(agentDir, 2)
                lrfSeq.append(FORWARD)

    return lrfSeq

# Main for testing. - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():
    # Start by defining udlr action sequences and their associated lrf action
    # sequence. Each sequence comes with a starting direction.
    udlrs = [
        ([0, 0, 0, 1, 1, 0, 0, 0], 0),
        ([3, 3, 2, 2, 1, 1, 0, 0], 1)
    ]
    lrfs = [
        [2, 2, 2, 1, 2, 2, 0, 2, 2, 2],
        [1, 1, 2, 2, 0, 2, 2, 0, 2, 2, 0, 2, 2]
    ]

    for i, seq in enumerate(udlrs):
        correct = udlr_to_lrf(seq[0], seq[1]) == lrfs[i]
        print(f"Seq {i} passes: {correct}")
        if not correct:
            print("  Pred:", udlr_to_lrf(seq[0], seq[1]))
            print("   Src:", lrfs[i])

if __name__ == '__main__':
    main()



