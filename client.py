from reader import FileReader
from checker import Checker
import csv

class Account():

    data = []
    cleaned_data = []

    def __init__(self):
        self.data = FileReader().readFile("client.csv")

    def clean(self):
        c = Checker()
        cur = set()
        for item in self.data:
            client_id = c.intChecker(item[0])
            birth_number = item[1]
            y = birth_number[0:2]
            m = birth_number[2:4]
            d = birth_number[4:6]
            m = c.intChecker(m)
            if (m > 50):
                m = m - 50
                gender = "female"
            else:
                gender = "male"
            m = str(m)
            birth_str = y + '/' + m + '/' + d
            birth, time = c.dateChecker(birth_str)
            district_id = c.intChecker(item[2])
            if birth == '-1' and time == '-1':
                print('date error', client_id)
                continue
            if not c.sameChecker(cur, client_id):
                self.cleaned_data.append([client_id, district_id, gender, birth])
                cur.add(client_id)
            else:
                print('primary key error', client_id)

    def output(self, fileName):
        f = open(fileName, 'w')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['card_id', 'disp_id', 'type', 'issue_date', 'issue_time'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    account = Account()
    # print(account.data)
    account.clean()
    account.output("cleaned_client.csv")
