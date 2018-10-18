from account import Account
from card import Card
from client import Client
from disp import Disp
from district import District
from loan import Loan
from order import Order
from trans import Trans

class Cleaner():

    account = Account()
    card = Card()
    client = Client()
    disp = Disp()
    district = District()
    loan = Loan()
    order = Order()
    trans = Trans()

    def cleanData(self):
        print("Error in district:")
        self.district.clean()
        self.district.output("cleaned_district.csv")
        print("Error in account:")
        self.account.clean(self.district.cur)
        self.account.output("cleaned_account.csv")
        print("Error in client:")
        self.client.clean(self.district.cur)
        self.client.output("cleaned_client.csv")
        print("Error in disp:")
        self.disp.clean(self.client.cur, self.account.cur)
        self.disp.output("cleaned_disp.csv")
        print("Error in card:")
        self.card.clean(self.disp.cur)
        self.card.output("cleaned_card.csv")
        print("Error in loan:")
        self.loan.clean(self.account.cur)
        self.loan.output("cleaned_loan.csv")
        print("Error in order:")
        self.order.clean(self.account.cur)
        self.order.output("cleaned_order.csv")
        print("Error in trans:")
        self.trans.clean(self.account.cur)
        self.trans.output("cleaned_trans.csv")


if __name__ == '__main__':
    c = Cleaner()
    c.cleanData()
