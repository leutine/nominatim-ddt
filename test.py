import nominatim as nom
import xlrd


def test_geocode():
    filename = "TestData/TestData_geocode.xls"
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        # print(row)
        try:
            coords = tuple(float(i) for i in str(row[1]).split(","))
        except ValueError:
            coords = row[1]
        print(row[0])
        geocode = nom.geocode(str(row[0]))
        if geocode == coords:
            print("Passed\n")
        else:
            print("Failed\n")


def test_reverse():
    filename = "TestData/TestData_reverse.xls"
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        location = str(row[1]).lower().split()
        # print(location)
        try:
            coords = tuple(float(i) for i in str(row[0]).split(","))
        except ValueError:
            coords = row[0]
        reverse = nom.reverse(coords[0], coords[1]).lower()
        print(reverse)
        if all(obj in reverse for obj in location):
            print("Passed\n")
        else:
            print("Failed\n")


# test_geocode()
test_reverse()
