import cell
import copy

class spreadsheet:
    def __init__(self, row: int, column: int):
        self.mat = []
        self.COLUMN = column
        self.ROW = row
        for i in range(row):
            self.mat.append([])
            for j in range(column):
                self.mat[i].append(cell.cell())

    def setCellAt(self, row: int, column: int, val):
        if isinstance(val, str):
            self.mat[row][column].value = val
        elif isinstance(val, cell.cell):
            self.mat[row][column] = copy.deepcopy(val)

    def getCellAt(self, row: int, column: int):
        if row >= 0 and row < len(self.mat) and column >= 0 and column < len(self.mat[0]):
            return self.mat[row][column]

    def addRow(self, row:int):
        self.mat.insert(row+1, [])
        for i in range(0, self.COLUMN):
            self.mat[row+1].append(cell.cell())
        self.ROW += 1

    def removeRow(self, row:int):
        self.mat.pop(row)

    def addColumn(self, column:int):
        for i in self.mat:
            i.insert(column+1, cell.cell())

    def removeColumn(self, column:int):
        for i in self.mat:
            i.pop(column)

    def swapRows(self, first:int, second:int):
        self.mat[first], self.mat[second] = self.mat[second], self.mat[first]

    def swapColumns(self, first:int, second:int):
        for i in self.mat:
            i[first], i[second] = i[second], i[first]
