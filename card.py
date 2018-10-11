from reader import FileReader
from checker import Checker
import csv

class Account():

    data = []
    cleaned_data = []

    def __init__(self):
        self.data = FileReader().readFile("card.csv")

    def clean(self):
        c = Checker()
        cur = set()
        for item in self.data:
            card_id = c.intChecker(item[0])
            disp_id = c.intChecker(item[1])
            type = item[2]
            date, time = c.dateChecker(item[3])
            if date == '-1' and time == '-1':
                print('date error', card_id)
                continue
            if not c.sameChecker(cur, card_id):
                self.cleaned_data.append([card_id, disp_id, type, date, time])
                cur.add(card_id)
            else:
                print('primary key error', card_id)

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
    account.output("cleaned_card.csv")
