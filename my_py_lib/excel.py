import xlrd


def read_excel(path):
    workbook = xlrd.open_workbook(path)
    sheet1 = workbook.sheet_by_name(workbook.sheet_names()[0])
    
    real_data = []
    for i in range(1, sheet1.ncols):
        real_data.append(sheet1.row_values(i))

    return (sheet1.row_values(0), real_data)

