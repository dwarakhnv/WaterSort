import os, sys
import copy
import json
from Bottle import Bottle


class WaterSort():


    def __init__(self, bottles:list=[]) -> None:
        self.BOTTLES = []
        self.MAX_BOTTLE_SIZE = 4
        self.OPERATIONS = []
        self.IS_SOLVED = False
        for bottle in bottles:
            self.add_bottle(bottle)
        self.validate()
        self.get_possible_operations()

    def add_bottle(self, colors:list, max_size=4):
        bottle = Bottle(colors, max_size=max_size)
        self.BOTTLES.append(bottle)

    def validate(self):
        color_value_map = {}
        for bottle in self.BOTTLES:
            for color in bottle.COLORS:
                if color in color_value_map:
                    color_value_map[color] += 1
                else:
                    color_value_map[color] = 1
        color_value_map = dict(sorted(color_value_map.items()))
        print(json.dumps(color_value_map, indent=4))

        if len(color_value_map.keys()) > (len(self.BOTTLES)-2):
            raise Exception(f"INVALID GAME SETUP. Number of colors found {len(color_value_map.keys())}, but should be >= {len(self.BOTTLES)-2}")
        
        for color, num in color_value_map.items():
            if num > 4:    # Allowing for partially known fields to validate incremental manual data entry
                raise Exception(f"INVALID GAME SETUP. Color Key {color} has {num} entries, but should have <= {self.MAX_BOTTLE_SIZE}")

        return True

    def _print_water_sort(self):
        for i in range(self.MAX_BOTTLE_SIZE):
            for bottle in self.BOTTLES:
                if len(bottle.COLORS) >= (self.MAX_BOTTLE_SIZE-i):
                    print(bottle.COLOR_BOX[self.MAX_BOTTLE_SIZE-1-i], end="  ")
                else:
                    print("__", end="  ")
            print()

    def is_solved(self):
        status = True
        for bottle in self.BOTTLES:
            status = status and (bottle.IS_SOLVED or bottle.IS_EMPTY)
        self.IS_SOLVED = status
        return status

    def get_possible_operations(self):
        operations = [] # [[1,2], [1,3], ...]

        if self.is_solved():
            self.OPERATIONS = operations
            # print("CONGRATS, You solved it!")
            return operations

        for i in range(len(self.BOTTLES)):
            i_top = self.BOTTLES[i].view_top()

            if i_top == []:
                continue
            if self.BOTTLES[i].IS_SOLVED:
                continue
            if self.BOTTLES[i].IS_EMPTY:
                continue

            for j in range(len(self.BOTTLES)):
                if i == j:
                    continue
                j_top = self.BOTTLES[j].view_top()
                j_space = self.BOTTLES[j].NUM_EMPTY

                if j_top != []:                    
                    if i_top[0] != j_top[0]:    # SAME COLOR 
                        continue

                if j_space < len(i_top):   # ENOUGH SPACE
                    continue

                if len(i_top) == len(self.BOTTLES[i].COLORS) and j_space == self.BOTTLES[j].MAX_SIZE:
                    continue

                operations.append([i, j])
        
        self.OPERATIONS = operations
        return operations
    
    def move(self, bottle1, bottle2):
        if [bottle1, bottle2] not in self.OPERATIONS:
            return None
        
        moving_colors = self.BOTTLES[bottle1].pop_top()
        self.BOTTLES[bottle2].add_top(moving_colors)
        self.get_possible_operations()
        
    def copy(self, water_sort):
        print(len(water_sort.BOTTLES))
        bottles = [
            list(copy.deepcopy(bottle.COLORS))
            for bottle in water_sort.BOTTLES
        ]
        print(len(bottles))
        water_sort_copy = WaterSort(bottles)
        print(len(water_sort_copy.BOTTLES))
        return water_sort_copy


if __name__ == "__main__":
    # python3 ./WaterSort.py

    bottle1 = [1, 1, 2, 2]
    bottle2 = [2, 2, 1, 1]
    bottle3 = []
    bottles = [bottle1, bottle2, bottle3]
    water_sort = WaterSort(bottles=bottles)
    water_sort._print_water_sort()
    print(water_sort.OPERATIONS)
    print("\n\n")

    water_sort.move(0, 2)
    water_sort._print_water_sort()
    print(water_sort.OPERATIONS)
    print("\n\n")


    water_sort.move(1, 0)
    water_sort._print_water_sort()
    print(water_sort.OPERATIONS)
    print("\n\n")

    water_sort.move(2, 1)
    water_sort._print_water_sort()
    print(water_sort.OPERATIONS)
    print("\n\n")


