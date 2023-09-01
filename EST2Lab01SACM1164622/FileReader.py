import json

def readCSVFile():
    data = [] 
    myFile = open(r'C:\Users\CASTA\Downloads\input.csv')
    print("The content of CSV file is:")
    text = myFile.readline()
    while text != "":
        print(text, end="")
        data.append(text)
        text = myFile.readline()
        
    myFile.close()
    return data
