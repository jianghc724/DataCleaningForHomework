from reader import FileReader
from checker import Checker
import csv

class Loan():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("loan.csv")

    def clean(self, account_id_set):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            loan_id = c.intChecker(item[0], i)
            account_id = c.intChecker(item[1], i)
            if not c.sameChecker(account_id_set, account_id):
                print('foreign key error Row', i)
            date, time = c.dateChecker(item[2], i)
            if date == '-1' and time == '-1':
                print('date error Row', i)
                continue
            amount = c.intChecker(item[3], i)
            duration = c.intChecker(item[4], i)
            payments = c.intChecker(item[5], i)
            if duration % 12 != 0:
                _d = duration
                y = duration % 12
                if y < 6:
                    duration = duration - y
                else:
                    duration = duration - y + 12
                print("Duration revision from", _d, "to", duration, "Row", i)
            if payments * duration != amount:
                _a = amount
                amount = payments * duration
                print("Amount revision from", _a, "to", amount, "Row", i)
            status = item[6]
            payduration = c.intChecker(item[7], i)
            if payduration > duration:
                print ("Payduration error Row", i)
                continue
            if not c.sameChecker(self.cur, loan_id):
                self.cleaned_data.append([loan_id, account_id, date, time, amount, duration, payments, status, payduration])
                self.cur.add(loan_id)
            else:
                print('primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['loan_id', 'account_id', 'date', 'time', 'amount', 'duration', 'payments', 'status', 'payduration'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    loan = Loan()
    # print(account.data)
    loan.clean(set(range(1,10000000)))
    loan.output("cleaned_loan.csv")
