from reader import FileReader
from checker import Checker
import csv

class Client():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("client.csv")

    def clean(self, district_id_set):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            client_id = c.intChecker(item[0], i)
            birth_number = item[1]
            y = birth_number[0:2]
            m = birth_number[2:4]
            d = birth_number[4:6]
            m = c.intChecker(m, i)
            if (m > 50):
                m = m - 50
                gender = "female"
            else:
                gender = "male"
            m = str(m)
            birth_str = y + '/' + m + '/' + d
            birth, time = c.dateChecker(birth_str, i)
            if birth == '-1' and time == '-1':
                print('Date error Row', i)
                continue
            birth_year = int(birth[0:4])
            age = 2000 - birth_year
            age_type = min(8, int(age / 10))
            district_id = c.intChecker(item[2], i)
            if not c.sameChecker(district_id_set, district_id):
                print('Foreign key district_id error Row', i)
                continue
            if not c.sameChecker(self.cur, client_id):
                self.cleaned_data.append([client_id, district_id, gender, birth, age, age_type])
                self.cur.add(client_id)
            else:
                print('Primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w', newline='')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['client_id', 'district_id', 'gender', 'birth', 'age', 'age_type'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    client = Client()
    # print(account.data)
    client.clean(set(range(1,10000000)))
    client.output("cleaned_client.csv")
