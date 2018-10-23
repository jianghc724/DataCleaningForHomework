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
        print("Error in client:")
        self.client.clean(self.district.cur)
        print("Error in disp:")
        self.disp.clean(self.client.cur, self.account.cur)
        dat = []
        i = 0
        j = 0
        k = 0
        a_len = len(self.account.cleaned_data)
        d_len = len(self.disp.cleaned_data)
        c_len = len(self.client.cleaned_data)
        while True:
            a = self.account.cleaned_data[i]
            d = self.disp.cleaned_data[j]
            c = self.client.cleaned_data[k]
            a_a_id = a[0]
            c_c_id = c[0]
            d_a_id = d[2]
            d_c_id = d[1]
            if a_a_id != d_a_id:
                while a_a_id < d_a_id:
                    account_id, district_id, frequency, date, time = a
                    g = 'unknown'
                    t = 'UNKNOWN'
                    dat.append([account_id, district_id, frequency, date, time, g, t])
                    i = i + 1
                    a = self.account.cleaned_data[i]
                    a_a_id = a[0]
                if a_a_id > d_a_id:
                    print("Sort error")
                    break
            if (c_c_id != d_c_id):
                print("Sort error")
                break
            g = c[2]
            t = d[3]
            if (j != d_len - 1) and (k != c_len - 1):
                _d = self.disp.cleaned_data[j + 1]
                _c = self.client.cleaned_data[k + 1]
                _d_a_id = _d[2]
                if d_a_id == _d_a_id:
                    _d_c_id = _d[1]
                    _c_c_id = _c[0]
                    if _c_c_id != _d_c_id:
                        print("Sort error")
                        break
                    _g = _c[2]
                    _t = _d[3]
                    if g != _g:
                        g = 'couple'
                    if t != _t:
                        t = 'DOUBLE'
                    j = j + 1
                    k = k + 1
            account_id, district_id, frequency, date, time = a
            dat.append([account_id, district_id, frequency, date, time, g, t])
            i = i + 1
            j = j + 1
            k = k + 1
            if (i == a_len) or (j == d_len) or (k == c_len):
                break
        self.account.cleaned_data = dat
        self.account.output("cleaned_account.csv")
        self.client.output("cleaned_client.csv")
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
