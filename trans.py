from reader import FileReader
from checker import Checker
import csv

class Trans():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("trans.csv")

    def clean(self, account_id_set):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            trans_id = c.intChecker(item[0], i)
            account_id = c.intChecker(item[1], i)
            if not c.sameChecker(account_id_set, account_id):
                print('Foreign key account_id error Row', i)
            date, time = c.dateChecker(item[2], i)
            if date == '-1' and time == '-1':
                print('Date error Row', i)
                continue
            type = c.strChecker(item[3], ["PRIJEM", "VYDAJ"], i)
            if type == "-1":
                print('String type error Row', i)
            operation = c.strChecker(item[4], ["VYBER KARTOU", "VKLAD", "PREVOD Z UCTU", "VYBER", "PREVOD NA UCET"], i)
            if operation == "-1":
                print('String operation error Row', i)
            amount = c.intChecker(item[5], i)
            balance = c.allintChecker(item[6], i)
            k_symbol = c.strChecker(item[7], [" ", "POJISTNE", "SLUZBY", "UROK", "SANKC. UROK", "SIPO", "DUCHOD", "UVER"], i)
            if k_symbol == "-1":
                print('String k_symbol error Row', i)
            bank = item[8]
            account = item[9]
            if not c.sameChecker(self.cur, trans_id):
                self.cleaned_data.append([trans_id, account_id, date, time, type, operation, amount, balance, k_symbol, bank, account])
                self.cur.add(trans_id)
            else:
                print('Primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w', newline='')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['trans_id', 'account_id', 'date', 'time', 'type', 'operation', 'amount', 'balance', 'k_symbol', 'bank', 'account'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    trans = Trans()
    # print(account.data)
    trans.clean(set(range(1,10000000)))
    trans.output("cleaned_trans.csv")
