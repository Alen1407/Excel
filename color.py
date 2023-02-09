import string

class color:
    def __init__(self, val:string):
        if val == "red" or "Red" or "RED":
            self.val = 0
        elif val == "blue" or "Blue" or "BLUE":
            self.val = 1
        elif val == "orange" or "Orange" or "ORANGE":
            self.val = 2
        elif val == "green" or "Green" or "GREEN":
            self.val = 3
        elif val == "black" or "Black" or "BLACK":
            self.val = 4
        else:
            self.val = None
