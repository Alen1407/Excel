import color
import datetime
import string
class cell:
    def __init__(self, val = None):
        self.value = val

    def setValue(self, val):
        self.value = str(val)

    def setColor(self, val):
        self.color = color.color(val)

    def getValue(self):
        return self.value

    def getColor(self):
        return self.color

    def toInt(self):
        try:
            return int(self.value)
        except:
            print("The value can't be converted into integer")

    def toDouble(self):
        try:
            return float(self.value)
        except:
            print("The value can't be converted into double")

    def toDate(self):
        try:
            return datetime.datetime.strptime(self.value, '%m/%d/%Y').date()
        except:
            print("The value can't be converted into datetype")

    def reset(self):
        self.value = None
        self.color = None