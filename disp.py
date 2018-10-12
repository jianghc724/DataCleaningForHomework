from reader import FileReader
from checker import Checker
import csv

class Disp():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("disp.csv")

    def clean(self, client_id_set, account_id_set):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            disp_id = c.intChecker(item[0], i)
            client_id = c.intChecker(item[1], i)
            if not c.sameChecker(client_id_set, client_id):
                print('Foreign key client_id error Row', i)
            account_id = c.intChecker(item[2], i)
            if not c.sameChecker(account_id_set, account_id):
                print('Foreign key account_id error Row', i)
            type = c.strChecker(item[3], ["OWNER", "DISPONENT"], i)
            if type == "-1":
                print('String error type Row', i)
            if not c.sameChecker(self.cur, disp_id):
                self.cleaned_data.append([disp_id, client_id, account_id, type])
                self.cur.add(disp_id)
            else:
                print('Primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['disp_id', 'client_id', 'account_id', 'type'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    disp = Disp()
    # print(account.data)
    disp.clean(set(range(1,10000000)), set(range(1,10000000)))
    disp.output("cleaned_disp.csv")
