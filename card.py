from reader import FileReader
from checker import Checker
import csv

class Card():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("card.csv")

    def clean(self):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            card_id = c.intChecker(item[0], i)
            disp_id = c.intChecker(item[1], i)
            type = item[2]
            date, time = c.dateChecker(item[3], i)
            if date == '-1' and time == '-1':
                print('date error Row', i)
                continue
            if not c.sameChecker(self.cur, card_id):
                self.cleaned_data.append([card_id, disp_id, type, date, time])
                self.cur.add(card_id)
            else:
                print('primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['card_id', 'disp_id', 'type', 'issue_date', 'issue_time'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    card = Card()
    # print(account.data)
    card.clean()
    card.output("cleaned_card.csv")
