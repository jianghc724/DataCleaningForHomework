import csv

class FileReader():
    def readFile(self, fileName):
        result = []
        if fileName.endswith(".csv"):
            csvFile = open(fileName, "r")
            reader = csv.reader(csvFile)
            for item in reader:
                if reader.line_num == 1:
                    continue
                result.append(item)
        return result

if __name__ == '__main__':
    fileName = "account.csv"
    r = FileReader()
    data = r.readFile(fileName)
    print (data)
