from reader import FileReader
from checker import Checker
import csv

class Order():

    data = []
    cleaned_data = []
    cur = set()

    def __init__(self):
        self.data = FileReader().readFile("order.csv")

    def clean(self, account_id_set):
        c = Checker()
        i = 0
        for item in self.data:
            i = i + 1
            order_id = c.intChecker(item[0], i)
            account_id = c.intChecker(item[1], i)
            if not c.sameChecker(account_id_set, account_id):
                print('Foreign key account_id error Row', i)
            bank_to = item[2]
            account_to = c.intChecker(item[3], i)
            amount = c.intChecker(item[4], i)
            k_symbol = c.strChecker(item[5], [" ", "POJISTNE", "SIPO", "LEASING", "UVER"], i)
            if k_symbol == "-1":
                print('String k_symbol error Row', i)
            if not c.sameChecker(self.cur, order_id):
                self.cleaned_data.append([order_id, account_id, bank_to, account_to, amount, k_symbol])
                self.cur.add(order_id)
            else:
                print('Primary key error Row', i)

    def output(self, fileName):
        f = open(fileName, 'w', newline='')
        csvwriter = csv.writer(f, dialect='excel')
        csvwriter.writerow(['order_id', 'account_id', 'bank_to', 'account_to', 'amount', 'k_symbol'])
        for item in self.cleaned_data:
            csvwriter.writerow(item)

if __name__ == '__main__':
    order = Order()
    # print(account.data)
    order.clean(set(range(1,10000000)))
    order.output("cleaned_order.csv")
