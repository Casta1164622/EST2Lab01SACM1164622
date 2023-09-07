import csv

def readCSVFile():
    result = [] 
    with open(r'C:\Users\CASTA\Downloads\input.csv') as csvfile:
        csvReader = csv.reader(csvfile, delimiter=';')
        for row in csvReader:
            result.append(row)
    return result
