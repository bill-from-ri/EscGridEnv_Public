#
# NLWMs.py
#   Author: Bill Xia
#   Created: March 3, 2025
#
# Purpose: Implements a helper function that returns transition information
#          about different configurations of EscGridEnv.
#

def get_NLWMs(lvl):
    '''
    Returns the gold-standard affordances for objects in the given level.
    '''
    if lvl == 'lvl_1':
        return {
            'green' : 'The green object is the Goal that the agent must reach.',
            'brown' : 'Brown objects are False Walls, which the agent can move through.'
        }
    elif lvl == 'lvl_3':
        return {
            'green'  : 'The green object is the Goal that the agent must reach.',
            'brown'  : ' '.join([
                'Brown objects are False Walls. The agent can move through',
                'False Walls.'
            ]),
            'orange' : ' '.join([
                'The orange object is a Crate. The agent can push the Crate by',
                'moving towards it while adjacent to the Crate.'
            ]),
            'pink'   : ' '.join([
                'The pink objects is a Button. When the Crate is pushed onto',
                'the Button, the ButtonDoor opens.'
            ]),
            'blue'   : ' '.join([
                'The blue object is a ButtonDoor. When the Crate is pushed onto',
                'the Button, the ButtonDoor opens. The agent cannot move',
                'through the ButtonDoor while it is closed.'
            ])
        }
    elif lvl.startswith('lvl_5'):
        return {
            'green'  : 'The green object is the Goal that the agent must reach.',
            'brown'  : ' '.join([
                'Brown objects are False Walls. The agent can move through',
                'False Walls.'
            ]),
            'yellow' : ' '.join([
                'The yellow object is a Key. The agent can pick up the Key',
                'by moving into its space. While holding the Key, the agent',
                'is colored purple.'
            ]),
            'cyan'   : ' '.join([
                'The cyan object is a KeyDoor. When the agent moves onto this',
                'object, the KeyDoor opens and the Key is destroyed. The agent',
                'cannot move through the KeyDoor while it is closed.'
            ])
        }
    elif lvl == 'lvl_9':
        return {
            'green'  : 'The green object is the Goal that the agent must reach.',
            'brown'  : ' '.join([
                'Brown objects are False Walls. The agent can move through',
                'False Walls.'
            ]),
            'orange' : ' '.join([
                'Orange objects are Crates. The agent can push a Crate by',
                'moving towards it while adjacent to that Crate.'
            ]),
            'pink'   : ' '.join([
                'The pink objects is a Button. When the Crate is pushed onto',
                'the Button, the ButtonDoor opens.'
            ]),
            'blue'   : ' '.join([
                'The blue object is a ButtonDoor. When the Crate is pushed onto',
                'the Button, the ButtonDoor opens. The agent cannot move',
                'through the ButtonDoor while it is closed.'
            ]),
            'yellow' : ' '.join([
                'The yellow object is a Key. The agent can pick up the Key',
                'by moving into its space. While holding the Key, the agent',
                'is colored purple.'
            ]),
            'cyan'   : ' '.join([
                'The cyan object is a KeyDoor. When the agent moves onto this',
                'object, the KeyDoor opens and the Key is destroyed. The agent',
                'cannot move through the KeyDoor while it is closed.'
            ])
        }
    elif lvl == 'lvl_11':
        return {
            'green'  : 'The green object is the Goal that the agent must reach.',
            'brown'  : ' '.join([
                'Brown objects are False Walls. The agent can move through',
                'False Walls.'
            ]),
            'orange' : ' '.join([
                'The orange object is a Crate. The agent can push the Crate by',
                'moving towards it while adjacent to the Crate.'
            ]),
            'pink'   : ' '.join([
                'The pink objects is a Button. When the Crate is pushed onto',
                'the Button, the ButtonDoor opens.'
            ]),
            'blue'   : ' '.join([
                'The blue object is a ButtonDoor. When the Crate is pushed onto',
                'the Button, the ButtonDoor opens. The agent cannot move',
                'through the ButtonDoor while it is closed.'
            ]),
            'grey'   : ' '.join([
                'Grey objects are Walls. The agent cannot move through these',
                'objects.'
            ])
        }
    elif lvl == 'lvl_12':
        return {
            'green'  : 'The green object is the Goal that the agent must reach.',
            'brown'  : ' '.join([
                'Brown objects are False Walls. The agent can move through',
                'False Walls.'
            ]),
            'orange' : ' '.join([
                'Orange objects are Crates. The agent can push a Crate by',
                'moving towards it while adjacent to that Crate. Pushing a',
                'Crate into a Key causes the Crate to absorb the Key, turning',
                'it into a purple KeyCrate.'
            ]),
            'yellow' : ' '.join([
                'The yellow object is a Key. The agent can pick up the Key',
                'by moving into its space. While holding the Key, the agent',
                'is colored purple. If the agent attempts to push an orange',
                'Crate while holding a Key, the Key is transferred to the Crate,'
                'which becomes a purple KeyCrate.'
            ]),
            'cyan'   : ' '.join([
                'The cyan object is a KeyDoor. When the agent moves onto this',
                'object, the KeyDoor opens and the Key is destroyed. The agent',
                'cannot move through the KeyDoor while it is closed.'
            ]),
            'purple' : ' '.join([
                'Purple objects are KeyCrates. The agent can push a KeyCrate by',
                'moving towards it while adjacent to that KeyCrate. Pushing',
                'a KeyCrate into an orange Crate causes the orange Crate to',
                'turn into a purple KeyCrate. Pushing a KeyCrate into a KeyDoor',
                'causes the KeyDoor to open. The KeyCrate then reverts into an',
                'orange Crate.'
            ])
        }