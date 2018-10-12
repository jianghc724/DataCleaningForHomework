from reader import FileReader
from checker import Checker
import csv

class Account():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("account.csv")

    def clean(self, district_id_set):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            account_id = c.intChecker(item[0], i)
            district_id = c.intChecker(item[1], i)
            if not c.sameChecker(district_id_set, district_id):
                print('Foreign key district_id error Row', i)
            frequency = c.strChecker(item[2], ["POPLATEK MESICNE", "POPLATEK TYDNE", "POPLATEK PO OBRATU"], i)
            if frequency == "-1":
                print('String frequency error Row', i)
            date, time = c.dateChecker(item[3], i)
            if date == '-1' and time == '-1':
                print('Date error Row', i)
                continue
            if not c.sameChecker(self.cur, account_id):
                self.cleaned_data.append([account_id, district_id, frequency, date, time])
                self.cur.add(account_id)
            else:
                print('Primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w', newline='')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['account_id', 'district_id', 'frequency', 'date', 'time'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    account = Account()
    # print(account.data)
    account.clean(set(range(1,10000000)))
    account.output("cleaned_account.csv")
