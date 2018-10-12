from reader import FileReader
from checker import Checker
import csv

class District():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("district.csv")

    def clean(self):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            district_id = c.intChecker(item[0], i)
            district_name = item[1]
            region = item[2]
            hab_number = c.intChecker(item[3], i)
            city_number = c.intChecker(item[4], i)
            ave_salary = c.intChecker(item[5], i)
            unemploy_rate = c.floatChecker(item[6], i)
            crime_number = c.intChecker(item[7], i)
            if not c.sameChecker(self.cur, district_id):
                self.cleaned_data.append([district_id, district_name, region, hab_number, city_number, ave_salary, unemploy_rate, crime_number])
                self.cur.add(district_id)
            else:
                print('primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['district_id', 'district_name', 'region', 'hab_number', 'city_number', 'ave_salary', 'unemploy_rate', 'crime_number'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    district = District()
    # print(account.data)
    district.clean()
    district.output("cleaned_district.csv")
