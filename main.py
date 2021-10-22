import itertools
import xlsxwriter

workbook = xlsxwriter.Workbook('my_excel.xlsx')
worksheet = workbook.add_worksheet()

a = [[0,1,2],
        [0,1,2],
        [0,1,2],
        [0,1,2],
        [0,1,2],
        [0,1,2],]

comb = (list(itertools.product(*a)))

for row, line in enumerate(comb):
    for col, cell in enumerate(line):
        worksheet.write(row, col, cell)

workbook.close()



