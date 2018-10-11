class Checker():
    def intChecker(self, s):
        if s.isdigit():
            return int(s)
        else:
            res = ""
            print(s)
            for c in s:
                if c.isdigit():
                    res = res + c
                else:
                    break
            print (res)
            return int(res)

    def dateChecker(self, s):
        l = s.split('/', 2)
        flag = True
        year = str(Checker.intChecker(self, l[0]))
        if len(year) != 4:
            if len(year) == 2:
                year = '19' + year
            else:
                return "-1", "-1"
        month = Checker.intChecker(self, l[1])
        if month >= 13:
            return "-1", "-1"
        l = l[2].split(' ', 1)
        day = Checker.intChecker(self, l[0])
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
        time = l[1].split(':', 1)
        hour = Checker.intChecker(self, time[0])
        minute = Checker.intChecker(self, time[1])
        if hour > 23:
            return "-1", "-1"
        if minute > 59:
            return "-1", "-1"
        hour = str(hour)
        minute = str(minute).zfill(2)
        date_res = year + '-' + month + '-' + day
        time_res = hour + ':' + minute
        return date_res, time_res

    def sameChecker(self, cur, new):
        if new in cur:
            return True
        else:
            return False
