import os, sys
import copy
import time
from WaterSort import WaterSort
from GameLevels import get_game


class Game():

    def __init__(self, bottles):
        self.WATER_SORT = WaterSort(bottles=bottles)

    def solve_game(self, game_state, game_copies=[], operation_steps=[]):   

        if game_state.IS_SOLVED:
            copy_steps = [ [step[0]+1, step[1]+1] for step in operation_steps]
            print("Steps :", len(operation_steps))
            print("SOLVED:", operation_steps)
            print("SOLVED Non-Zero:", copy_steps, "\n")
            for i in range(len(copy_steps)):
                print(copy_steps[i], end=", ")
                if (i+1) % 10 == 0:
                    print()
            print()

            for game in game_copies+[game_state]:
                print()
                game._print_water_sort()
            return True

        if len(operation_steps) >= 500:
            print("TRIED 500 MOVES!!!")
            return False

        operations = game_state.OPERATIONS
        if len(operations) == 0:
            return False

        for operation in operations:
            copy_game_state = copy.deepcopy(game_state)
            copy_game_state.get_possible_operations()
            copy_game_state.move(operation[0], operation[1])
            status = self.solve_game(copy_game_state, 
                    game_copies=game_copies + [game_state],
                    operation_steps=operation_steps + [operation])
            if status == True:
                return True

        return False



if __name__ == "__main__":
    # python3 ./Game.py GAME_NUM 
    # python3 ./Game.py GAME_NUM > FILE_GAME_NUM.txt

    game_number = sys.argv[1]
    print(game_number)

    start_time = time.time()

    game = Game(bottles=get_game(game_number))
    game.WATER_SORT._print_water_sort()
    game.WATER_SORT.validate()
    game.solve_game(game.WATER_SORT, [])

    total_time = time.time() - start_time
    print(f"Took {total_time} seconds")
