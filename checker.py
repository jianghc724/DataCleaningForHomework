import re

class Checker():
    def allintChecker(self, s, idx):
        flag = False
        if s[0] == "-":
            s = s[1:]
            flag = True
        res = Checker.intChecker(self, s, idx)
        if flag:
            return -res
        else:
            return res

    def intChecker(self, s, idx):
        if s.isdigit():
            return int(s)
        else:
            res = ""
            _s = s
            if s[0] == "-":
                s = s[1:]
            for c in s:
                if c.isdigit():
                    res = res + c
                else:
                    break
            print ("Int revision from", _s, "to", res, "Row", idx)
            return int(res)

    def floatChecker(self, s, idx):
        l = s.split('.', 1)
        l1 = Checker.intChecker(self, l[0], idx)
        l2 = Checker.intChecker(self, l[1], idx)
        s = str(l1) + '.' + str(l2)
        return float(s)

    def dateChecker(self, s, idx):
        l = re.split('[/-]', s, 2)
        year = str(Checker.intChecker(self, l[0], idx))
        if len(year) != 4:
            if len(year) == 2:
                year = '19' + year
            else:
                return "-1", "-1"
        month = Checker.intChecker(self, l[1], idx)
        if (month >= 13) or (month == 0):
            return "-1", "-1"
        l = l[2].split(' ', 1)
        day = Checker.intChecker(self, l[0], idx)
        if (day > 31) or (day == 0):
            return "-1", "-1"
        if month == 2:
            if (day == 30) or (day == 31):
                return "-1", "-1"
            if day == 29:
                if int(year) % 4 != 0:
                    return "-1", "-1"
                if int(year) % 100 == 0:
                    if int(year) % 400 != 0:
                        return "-1", "-1"
        if (month == 4) or (month == 6) or (month == 9) or (month == 11):
            if day == 31:
                return "-1", "-1"
        month = str(month)
        day = str(day)
        date_res = year + '-' + month + '-' + day
        if len(l) == 1:
            time_res = "0:00:00"
        else:
            time = l[1].split(':')
            hour = Checker.intChecker(self, time[0], idx)
            minute = Checker.intChecker(self, time[1], idx)
            second = 0
            flag = False
            if len(time) > 3:
                flag = True
                second = Checker.intChecker(self, time[2], idx)
            elif len(time) == 3:
                second = Checker.intChecker(self, time[2], idx)
            if hour > 23:
                return "-1", "-1"
            if minute > 59:
                return "-1", "-1"
            if second > 59:
                return "-1", "-1"
            hour = str(hour)
            minute = str(minute).zfill(2)
            second = str(second).zfill(2)
            time_res = hour + ':' + minute + ':' + second
            if flag:
                print ("Time revision from", time, "to", time_res, "Row", idx)
        return date_res, time_res

    def sameChecker(self, cur, new):
        if new in cur:
            return True
        else:
            return False
