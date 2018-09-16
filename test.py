import nominatim as nom
import xlrd


def test_geocode():
    filename = "TestData/TestData.xls"
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        try:
            coords = tuple(float(i) for i in str(row[1]).split(","))
        except ValueError:
            coords = row[1]
        print(row[0])
        geocode = nom.geocode(str(row[0]))
        if geocode == coords:
            print("Passed")
        else:
            print("Failed")


test_geocode()
