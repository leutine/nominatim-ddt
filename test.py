import nominatim as nom
import xlrd


def test_geocode():
    filename = "TestData/TestData_geocode.xls"
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        # print(row)
        # Преобразование значения из ячейки таблицы в кортеж (float,float)
        # для сравнения с результатом вывода geocode(str)
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
        # Преобразование значения из ячейки таблицы в кортеж (float,float),
        # которые далее будут выступать в качестве параметра reverse(float,float)
        try:
            coords = tuple(float(i) for i in str(row[0]).split(","))
        except ValueError:
            coords = row[0]
        reverse = nom.reverse(coords[0], coords[1]).lower()
        print(reverse)
        # Если в строке, полученной из reverse(float,float) есть ВСЕ строки,
        # взятые из ячейки ожидаемого результата в таблице, то тест будет считаться пройденным
        # (Знаю, что это неидеальное решение)
        if all(obj in reverse for obj in location):
            print("Passed\n")
        else:
            print("Failed\n")


def main():
    while True:
        try:
            option = int(input("Geocoding test (1)\nReverse geocoding test (2)\nEnter option: "))
            break
        except ValueError:
            print("That's not a valid option!\n")

    if option == 1:
        print("<Geocoding test>")
        test_geocode()
    elif option == 2:
        print("<Reverse geocoding test>")
        test_reverse()
    else:
        print("Invalid option!")


main()
