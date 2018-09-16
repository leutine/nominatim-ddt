import nominatim as nom
import xlrd


def test_geocode():
    filename = "TestData/TestData_geocode.xls"
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    passed = 0
    failed = 0
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        # print(row)
        # Преобразование значения из ячейки таблицы в кортеж (float,float)
        # для сравнения с результатом вывода geocode(str)
        try:
            coords = tuple(float(i) for i in str(row[1]).split(","))
        except ValueError:
            coords = row[1]
        # print(row[0])
        try:
            geocode = nom.geocode(str(row[0]))
        except AttributeError as e:
            print(e)
            return
        if geocode == coords:
            print("Passed\n")
            passed += 1
        else:
            print("Failed\n")
            failed += 1
    print("Number of tests: ", passed + failed,
          "\nTests passed: ", passed, " / ", round(passed / (passed + failed) * 100, 0), "%",
          "\nTests failed: ", failed, " / ", round(failed / (passed + failed) * 100, 0), "%")


def test_reverse():
    filename = "TestData/TestData_reverse.xls"
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(0)
    passed = 0
    failed = 0
    for row_num in range(sheet.nrows):
        row = sheet.row_values(row_num)
        location = str(row[1]).lower().split()
        # print(location)
        # Преобразование значения из ячейки таблицы в кортеж (float,float),
        # значения которого далее будут выступать в качестве параметров reverse(float,float)
        try:
            coords = tuple(float(i) for i in str(row[0]).split(","))
        except ValueError:
            coords = row[0]
        try:
            reverse = nom.reverse(coords[0], coords[1]).lower()
        except AttributeError as e:
            print(e)
            return
        # print(reverse)
        # Если в строке, полученной из reverse(float,float) есть ВСЕ строки,
        # взятые из ячейки ожидаемого результата в таблице, то тест будет считаться пройденным
        # (Знаю, что это далеко не идеальное решение)
        if all(obj in reverse for obj in location):
            print("Passed\n")
            passed += 1
        else:
            print("Failed\n")
            failed += 1
    print("Number of tests: ", passed + failed,
          "\nTests passed: ", passed, " / ", round(passed/(passed + failed)*100, 0), "%",
          "\nTests failed: ", failed, " / ", round(failed/(passed + failed)*100, 0), "%")


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
