import xlrd


def test():
    filename = "TestData/TestData.xls"
    xls = xlrd.open_workbook(filename)
    print(xls)


test()
