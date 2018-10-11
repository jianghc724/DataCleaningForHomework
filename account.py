from reader import FileReader
from checker import Checker
import csv

class Account():

    data = []
    cleaned_data = []

    def __init__(self):
        self.data = FileReader().readFile("account.csv")

    def clean(self):
        c = Checker()
        for item in self.data:
            account_id = c.intChecker(item[0])
            district_id = c.intChecker(item[1])
            frequency = item[2]
            date, time = c.dateChecker(item[3])
            if date == '-1' and time == '-1':
                pass
            self.cleaned_data.append([account_id, district_id, frequency, date, time])

    def output(self, fileName):
        f = open(fileName, 'w')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['account_id', 'district_id', 'frequency', 'date', 'time'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    account = Account()
    # print(account.data)
    account.clean()
    account.output("cleaned_account.csv")
