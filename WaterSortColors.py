import os, sys


class Color():

    # 🔴🟠🟡🟢🔵🟣🟤⚫⚪
    # 🟥🟧🟨🟩🟦🟪🟫⬛⬜
    # ❓🍔🍟🍕🥪

    MAP = {
        -1:"❓",
        0:"⬛",
        1:"🟥",
        2:"🌸",
        3:"🟩",
        4:"💎",
        5:"🥎",
        6:"🟦",
        7:"🟨",
        8:"🟪",
        9:"🟧",
        10:"💸",
        11:"🟫",
        12:"🍔",
        13:"🍟",
        14:"🍕",
    }

    def __init__(self, color:int):
        self.COLOR = color
        self.COLOR_BOX = self.MAP[color]

    def __str__(self):
        return self.COLOR_BOX
        
