#
# levels.py
#   Author: Bill Xia
#   Created: 9/19/24
#
# Purpose: Defines a collection of grid_layouts, which are 2D string lists that
#          represent configurations of an EscGridEnv environment. The layouts
#          in this file represent configurations of levels as seen in Professor
#          Sarathy's puzzle paper.
#

# Constants.
WAL = 'w'
FWL = 'f'
GOL = 'g'
CRT = 'c'
BTN = 'p'
BDR = 'd'
KEY = 'k'
KDR = 't'
emp = ''

# Debugging function.
def debugLayout(layout):
    for row in layout:
        for cell in row:
            if cell == emp:
                print('. ', end='')
            else:
                print(cell, end=' ')
        print()

# Level 1
def lvl_1():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_1_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 2
def lvl_2():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_2_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 3
def lvl_3():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, CRT, emp, emp, BTN, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_3_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, CRT, emp, emp, BTN, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 4
def lvl_4():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, BTN, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, CRT, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_4_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, BTN, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, CRT, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 5
def lvl_5():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_5_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 5
def lvl_5b():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
# Level 5
def lvl_5c():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 5
def lvl_5d():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 5
def lvl_5e():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 6
def lvl_6():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, KDR, KDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_6_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, KDR, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 7
def lvl_7():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, KDR, KDR, KDR, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, KDR, KEY, KDR, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, KDR, KDR, KDR, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_7_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, emp, emp, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, KDR, KDR, KDR, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, KDR, KEY, KDR, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, KDR, KDR, KDR, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 8
def lvl_8():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, KDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, KEY, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_8_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, KEY, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 9
def lvl_9():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, KDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, KEY, emp, CRT, emp, emp, emp, BTN, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_9_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, KEY, emp, CRT, emp, emp, emp, BTN, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 10
def lvl_10():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, CRT, CRT, KEY, CRT, CRT, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, KDR, GOL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BTN, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env
def lvl_10_rand():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, CRT, CRT, KEY, CRT, CRT, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, CRT, CRT, CRT, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, KDR, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BTN, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 11
def lvl_11():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, WAL, WAL, WAL],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, GOL, WAL, WAL],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, WAL, WAL, WAL],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, BTN, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 12
def lvl_12():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, WAL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, CRT, emp, WAL, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, KEY, emp, emp, CRT, CRT, KDR, GOL, WAL, WAL],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, CRT, emp, WAL, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, WAL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, CRT, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 13a
def lvl_13a():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, emp, KEY, emp, CRT, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, emp, CRT, emp, CRT, WAL, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, emp, CRT, emp, CRT, WAL, WAL, WAL, WAL],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, emp, KDR, KDR, KDR, GOL, emp, WAL],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, CRT, emp, CRT, emp, CRT, WAL, WAL, WAL, WAL],
           [emp, emp, emp, FWL, emp, KDR, KDR, KDR, emp, emp, emp, emp, emp, emp, CRT, emp, CRT, emp, CRT, WAL, emp, emp],
           [emp, emp, emp, FWL, emp, KDR, KEY, KDR, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, KDR, KDR, KDR, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

# Level 13b
def lvl_13b():
    #       0    1    2    3    4    5    6    7    8    9    10   11   12   13   14   15   16   17   18   19   20   21
    env = [[emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, CRT, CRT, emp, emp, CRT, emp, emp, emp, emp, WAL, WAL, WAL, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, BDR, KDR, GOL, WAL, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, WAL, WAL, WAL, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, CRT, emp, emp, emp, CRT, WAL, KDR, WAL, CRT, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, CRT, KEY, CRT, emp, emp, CRT, KDR, BTN, KDR, CRT, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, CRT, emp, emp, emp, CRT, WAL, KDR, WAL, CRT, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, CRT, CRT, CRT, CRT, CRT, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, FWL, emp, emp, emp],
           [emp, emp, emp, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, FWL, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp],
           [emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp, emp]]
    return env

if __name__ == '__main__':
    print('Environment Visualization:')
    debugLayout(lvl_13a())



