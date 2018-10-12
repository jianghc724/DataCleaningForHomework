from reader import FileReader
from checker import Checker
import csv

class Disp():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("disp.csv")

    def clean(self):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            disp_id = c.intChecker(item[0], i)
            client_id = c.intChecker(item[1], i)
            account_id = c.intChecker(item[2], i)
            type = item[3]
            if not c.sameChecker(self.cur, disp_id):
                self.cleaned_data.append([disp_id, client_id, account_id, type])
                self.cur.add(disp_id)
            else:
                print('primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['disp_id', 'client_id', 'account_id', 'type'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    disp = Disp()
    # print(account.data)
    disp.clean()
    disp.output("cleaned_disp.csv")