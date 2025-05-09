#
# NewObjects.py
#   Author: Bill Xia
#   Created: 9/9/2024
#
# Purpose: Defines a collection of new MiniGrid World Objects, which will be
#          used to create the EscapeWorld MiniGrid environment.
#

from minigrid.core.world_object import WorldObj
from minigrid.core.world_object import Goal, Wall
from minigrid.core.constants import (
    COLORS,
    IDX_TO_OBJECT,
    IDX_TO_COLOR
)
from minigrid.utils.rendering import (
    fill_coords,
    point_in_rect,
)

# EscObj.
# Same as a WorldObj, but with extra code in the decode function.
class EscObj(WorldObj):
    @staticmethod
    def decode(type_idx: int, color_idx: int, state: int) -> WorldObj | None:
        """Create an object from a 3-tuple state description"""

        obj_type = IDX_TO_OBJECT[type_idx]
        color = IDX_TO_COLOR[color_idx]

        if obj_type == "empty" or obj_type == "unseen" or obj_type == "agent":
            return None

        # State, 0: open, 1: closed, 2: locked
        is_open = state == 0
        is_locked = state == 2

        if obj_type == "wall":
            v = Wall(color)
        elif obj_type == "goal":
            v = Goal()
        elif obj_type == "crate":
            v = Crate(color)
        elif obj_type == "plate":
            v = Button(color)
        elif obj_type == "plateDoor":
            v = ButtonDoor(color)
        elif obj_type == "escKey":
            v = PuzzleKey(color)
        elif obj_type == "escKeyDoor":
            v = PuzzleKeyDoor(color)
        elif obj_type == "falseWall":
            v = FalseWall(color)
        else:
            assert False, "unknown object type in decode '%s'" % obj_type

        return v

# Crate.
# Can be pushed by the player.
class Crate(EscObj):
    def __init__(self, color: str = 'orange'):
        super().__init__('crate', color)

        # The cell that the Crate is currently top of and the last cell that
        # the Crate was on top of.
        self.underneath = None
        self.behind = None

        # The Crate can become a KeyCrate if it is pushed into a PuzzleKey.
        self.is_keyCrate = False

    def can_overlap(self):
        return False

    def can_pickup(self):
        return False

    def render(self, img):
        c = COLORS[self.color]

        # Fill
        fill_coords(img, point_in_rect(0, 1, 0, 1), c)

    # New function used for pushing.
    def push(self, env, pos, direction):
        # Compute new position.
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        try:
            new_cell = env.grid.get(*new_pos)
        except:
            return False

        # If new position is empty or overlappable...
        if new_cell is None or new_cell.can_overlap_crate():
            # Save the cell we're about to run over.
            self.behind = self.underneath
            self.underneath = new_cell
            # Change position.
            env.grid.set(*new_pos, self)
            if isinstance(self.behind, PuzzleKey):
                env.grid.set(*pos, None)
            else:
                env.grid.set(*pos, self.behind)
            return True

        # If we are trying to merge with a Key...
        elif isinstance(new_cell, PuzzleKey) and not self.is_keyCrate:
            # Destroy the key.
            env.grid.set(*new_pos, None)
            # Activate crate.
            self.is_keyCrate = True
            self.color = 'purple'

        # If we are trying to unlock a KeyDoor...
        elif isinstance(new_cell, PuzzleKeyDoor) and self.is_keyCrate:
            # Unlock door.
            env.grid.set(*new_pos, None)
            # Deactivate crate.
            self.is_keyCrate = False
            self.color = 'orange'

        # If we are pushing into another Crate...
        elif isinstance(new_cell, Crate):
            # First check if this is a keyCrate...
            if self.is_keyCrate and not new_cell.is_keyCrate:
                new_cell.is_keyCrate = True
                new_cell.color = 'purple'
            # Next check if the agent is carrying a key...
            elif env.carrying is not None:
                # Update crate.
                self.is_keyCrate = True
                self.color = 'purple'
                # Update agent.
                env.carrying = None
                env.grid.make_agent_red()

        # Otherwise...
        return False

# Button.
# When a Crate is pushed onto a Button, the Button opens a paired ButtonDoor.
class Button(EscObj):
    def __init__(self, color: str = 'pink'):
        super().__init__('plate', color)
        self.is_activated = False

    def can_overlap(self):
        return True

    def can_pickup(self):
        return False

    def render(self, img):
        c = COLORS[self.color]

        # Fill
        fill_coords(img, point_in_rect(0, 1, 0, 1), c)

    def can_overlap_crate(self):
        return True
    
    def toggle(self, env, pos):
        self.is_activated = not self.is_activated
        return True

# ButtonDoor.
# Opens when Create is pushed onto a paired Button. Closed otherwise.
class ButtonDoor(EscObj):
    def __init__(self, color: str = 'blue'):
        super().__init__('plateDoor', color)
        self.is_open = False

    def can_overlap(self):
        return self.is_open

    def can_pickup(self):
        return False

    def render(self, img):
        c = COLORS[self.color]

        # print('  RENDERING BUTTONDOOR')
        # if self.is_open:
        #     print('  BUTTONDOOR OPEN\n')
        # else:
        #     print('  BUTTONDOOR CLOSED\n')

        # Fill
        if self.is_open:
            fill_coords(img, point_in_rect(0.5, 0.5, 0.5, 0.5), COLORS['null'])
        else:
            fill_coords(img, point_in_rect(0, 1, 0, 1), c)

    def can_overlap_crate(self):
        return self.is_open

    def open_door(self):
        self.is_open = True
        return True

    def close_door(self):
        self.is_open = False
        return True

# PuzzleKey.
# Walking into a PuzzleKey allows the player to open a PuzzleKeyDoor.
# Pushing a crate onto a PuzzleKey causes them to combine and turn into a
#   KeyCrate.
class PuzzleKey(EscObj):
    def __init__(self, color: str = 'yellow'):
        super().__init__('escKey', color)

    def can_overlap(self):
        return False

    def can_pickup(self):
        return False

    def render(self, img):
        c = COLORS[self.color]

        # Fill
        fill_coords(img, point_in_rect(0, 1, 0, 1), c)

    # def can_overlap_crate(self):
    #     return True

# PuzzleKeyDoor.
# A player with a PuzzleKey opens this door by walking into it.
# Pushing a KeyCrate into a PuzzleKeyDoor causes that door to open.
class PuzzleKeyDoor(EscObj):
    def __init__(self, color: str = 'cyan'):
        super().__init__('escKeyDoor', color)

    def can_overlap(self):
        return False

    def can_pickup(self):
        return False

    def render(self, img):
        c = COLORS[self.color]

        # Fill
        fill_coords(img, point_in_rect(0, 1, 0, 1), c)

# FalseWall.
# Functionally the same as a Floor, but with different rendering code.
class FalseWall(EscObj):
    def __init__(self, color: str = 'brown'):
        super().__init__('falseWall', color)

    def can_overlap(self):
        return True

    def can_pickup(self):
        return False

    def render(self, img):
        c = COLORS[self.color]

        # Fill
        fill_coords(img, point_in_rect(0, 1, 0, 1), c)

    def can_overlap_crate(self):
        return True



