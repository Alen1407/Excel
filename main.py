import Tester
import spreadsheet

test = Tester.Tester()
test.testAll()
print()
sp = spreadsheet.spreadsheet(3, 5)
sp.setCellAt(2,1,"hey")
sp.setCellAt(1,1,-5)
sp.addRow(0)
sp.addColumn(0)
sp.removeRow(0)
sp.printSpreadsheet()
