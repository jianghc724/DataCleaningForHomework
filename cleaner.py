from account import Account
from card import Card
from client import Client
from disp import Disp
from district import District
from loan import Loan
from order import Order
from trans import Trans

class Cleaner():
    def cleanData(self):
        account = Account()
        card = Card()
        client = Client()
        disp = Disp()
        district = District()
        loan = Loan()
        order = Order()
        trans = Trans()
        print("Error in district:")
        district.clean()
        district.output("cleaned_district.csv")
        print("Error in account:")
        account.clean(district.cur)
        account.output("cleaned_account.csv")
        print("Error in client:")
        client.clean(district.cur)
        client.output("cleaned_client.csv")
        print("Error in disp:")
        disp.clean(client.cur, account.cur)
        disp.output("cleaned_disp.csv")
        print("Error in card:")
        card.clean(disp.cur)
        card.output("cleaned_card.csv")
        print("Error in loan:")
        loan.clean(account.cur)
        loan.output("cleaned_loan.csv")
        print("Error in order:")
        order.clean(account.cur)
        order.output("cleaned_order.csv")
        print("Error in account:")
        trans.clean(account.cur)
        trans.output("cleaned_trans.csv")


if __name__ == '__main__':
    c = Cleaner()
    c.cleanData()
