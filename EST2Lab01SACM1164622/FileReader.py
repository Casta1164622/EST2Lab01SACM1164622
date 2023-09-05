import json

def readCSVFile():
    data = [] 
    myFile = open(r'C:\Users\CASTA\Downloads\input.csv')
    text = myFile.readline()
    while text != "":
        data.append(text)
        text = myFile.readline()
        
    myFile.close()
    return data
