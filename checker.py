import re
import numpy as np

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

    def strChecker(self, s, strs, idx):
        for _s in strs:
            if s == _s:
                return s
        min_s = ""
        min_d = 100
        for _s in strs:
            m = len(s)
            n = len(_s)
            dist = np.zeros((m + 1, n + 1))
            for i in range(0, m + 1):
                dist[i][0] = i
            for j in range(0, n + 1):
                dist[0][j] = j
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    cost = 0
                    if s[i - 1] != _s[j - 1]:
                        cost = 1
                    deletion = dist[i - 1][j] + 1
                    insertion = dist[i][j - 1] + 1
                    substitution = dist[i - 1][j - 1] + cost
                    dist[i][j] = min(deletion, insertion, substitution)
            if dist[m][n] < min_d:
                min_d = dist[m][n]
                min_s = _s
        if min_d <= 3:
            print ("String revision from", s, "to", _s, "Row", idx)
            return _s
        else:
            return "-1"
