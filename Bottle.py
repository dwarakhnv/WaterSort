import os, sys
from WaterSortColors import Color

class Bottle():

    MAX_SIZE    = 4
    COLORS      = []
    COLOR_BOX   = []
    IS_EMPTY    = None
    IS_FULL     = None
    IS_SOLVED   = False
    NUM_EMPTY   = None


    def __init__(self, colors, max_size=4):
        self.MAX_SIZE = max_size
        self.COLORS = colors
        self.status()

    def set_color_box(self):
        self.COLOR_BOX = []
        for color in self.COLORS:
            self.COLOR_BOX.append(Color(color))

    def pop_top(self):
        if self.IS_SOLVED:
            return []
        top_colors = self.view_top()
        self.COLORS = self.COLORS[:len(self.COLORS)-len(top_colors)]
        self.status()
        return top_colors
    
    def add_top(self, colors):
        self.COLORS.extend(colors)
        self.status()

    def view_top(self):
        if len(self.COLORS) == 0:
            return []
        color = self.COLORS[-1]
        top_color_list = [color]
        for i in range(len(self.COLORS)-1):
            next_color = self.COLORS[len(self.COLORS)-2-i]
            if color == next_color:
                top_color_list.append(next_color)
            else:
                break
        return top_color_list

    def status(self):
        assert len(self.COLORS) <= self.MAX_SIZE
        self.set_color_box()

        if len(self.COLORS) == 0:
            self.IS_EMPTY = True
        else:
            self.IS_EMPTY = False

        if len(self.COLORS) == self.MAX_SIZE:
            self.IS_FULL = True
        else:
            self.IS_FULL = False
            self.IS_SOLVED = False

        self.NUM_EMPTY = self.MAX_SIZE - len(self.COLORS)

        if self.IS_FULL:
            solved_bool = True
            temp_color = self.COLORS[0] 
            for i in range(self.MAX_SIZE):
                solved_bool = solved_bool and (self.COLORS[i] == temp_color)
            self.IS_SOLVED = solved_bool

    def _print_status(self):
        print(f"COLORS      : {self.COLORS}")
        print(f"MAX_SIZE    : {self.MAX_SIZE}")
        print(f"IS_EMPTY    : {self.IS_EMPTY}")
        print(f"IS_FULL     : {self.IS_FULL}")
        print(f"IS_SOLVED   : {self.IS_SOLVED}")
        print(f"NUM_EMPTY   : {self.NUM_EMPTY}")
        print(f"")
        

if __name__ == "__main__":
    # python3 ./Bottle.py

    max_size = 4
    colors = [3, 3, 3, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()

    colors = [1, 3, 3, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()

    colors = [1, 1, 3, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = [1, 1, 1, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = [3, 3, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = [1, 3, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = [1, 1, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = [3, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = [1, 3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = [3]
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
    
    colors = []
    bottle = Bottle(colors, max_size=max_size)
    print(bottle.view_top())
    bottle._print_status()
