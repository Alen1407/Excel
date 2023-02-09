import cell
import spreadsheet
import color

class Tester:
    def __init__(self, row:int = 5, column:int = 5):
        self.cell = cell.cell()
        self.spreadsheet = spreadsheet.spreadsheet(row, column)

    def print_whether_passed(self, bl:bool, func):
        if bl:
            print("Test " + func.__name__ + "() passed")
        else:
            print("Test " + func.__name__ + "() failed")

    def testCellSetValue(self, val:int):
        self.cell.setValue(str(val))
        self.print_whether_passed(self.cell.value == str(val), self.cell.setValue)

    def testCellSetColor(self):
        self.cell.setColor("red")
        self.print_whether_passed(self.cell.color.val == 0, self.cell.setColor)

    def testCellGetValue(self):
        self.print_whether_passed(self.cell.getValue() == self.cell.value, self.cell.getValue)

    def testCellGetColor(self):
        self.print_whether_passed(self.cell.getColor() == self.cell.color, self.cell.getColor)

    def testCellToInt(self):
        self.cell.setValue("-42")
        self.print_whether_passed(self.cell.toInt() == -42, self.cell.toInt)

    def testCellToDouble(self):
        self.cell.value = "2.14"
        self.print_whether_passed(self.cell.toDouble() == 2.14, self.cell.toDouble)

    def testCellReset(self):
        self.cell.reset()
        self.print_whether_passed((self.cell.value == None and self.cell.color == None), self.cell.reset)

    def testSpreadsheetSetCellAt(self):
        self.spreadsheet.setCellAt(1, 1, "hey")
        self.print_whether_passed(self.spreadsheet.mat[1][1].value == "hey", self.spreadsheet.setCellAt)

    def testSpreadsheetGetCellAt(self):
        self.print_whether_passed(self.spreadsheet.getCellAt(1,1) == self.spreadsheet.mat[1][1], self.spreadsheet.getCellAt)

    def testSpreadsheetAddRow(self):
        self.spreadsheet.mat[2][0].setValue("1")
        self.spreadsheet.addRow(1)
        self.print_whether_passed(self.spreadsheet.mat[2][0] != "1", self.spreadsheet.addRow)

    def testSpreadsheetAddColumn(self):
        self.spreadsheet.mat[0][2].setValue("1")
        self.spreadsheet.addColumn(1)
        self.print_whether_passed(self.spreadsheet.mat[0][2] != "1", self.spreadsheet.addColumn)

    def testSpreadsheetRemoveRow(self):
        temp = self.spreadsheet.mat[2]
        self.spreadsheet.removeRow(2)
        self.print_whether_passed(self.spreadsheet.mat[2] != temp, self.spreadsheet.removeRow)

    def testSpreadsheetRemoveColumn(self):
        temp = self.spreadsheet.mat[0][0]
        self.spreadsheet.removeColumn(0)
        self.print_whether_passed(self.spreadsheet.mat[0][0] != temp, self.spreadsheet.removeColumn)

    def testSpreadsheetSwapRows(self):
        temp = self.spreadsheet.mat[1]
        temp1 = self.spreadsheet.mat[2]
        self.spreadsheet.swapRows(1,2)
        self.print_whether_passed((temp == self.spreadsheet.mat[2] and temp1 == self.spreadsheet.mat[1]), self.spreadsheet.swapRows)

    def testSpreadsheetSwapColumns(self):
        temp = self.spreadsheet.mat[1][0]
        temp1 = self.spreadsheet.mat[1][1]
        self.spreadsheet.swapColumns(0,1)
        self.print_whether_passed((temp == self.spreadsheet.mat[1][1] and temp1 == self.spreadsheet.mat[1][0]), self.spreadsheet.swapColumns)

    def testAll(self):
        self.testCellSetValue(3)
        self.testCellSetColor()
        self.testCellGetValue()
        self.testCellGetColor()
        self.testCellToInt()
        self.testCellToDouble()
        self.testCellReset()
        self.testSpreadsheetSetCellAt()
        self.testSpreadsheetGetCellAt()
        self.testSpreadsheetAddRow()
        self.testSpreadsheetAddColumn()
        self.testSpreadsheetRemoveRow()
        self.testSpreadsheetRemoveColumn()
        self.testSpreadsheetSwapRows()
        self.testSpreadsheetSwapColumns()