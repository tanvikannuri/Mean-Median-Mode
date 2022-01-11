import csv

with open('SOCR-HeightWeight.csv', newline='') as file:
    reader = csv.reader(file)
    fileData = list(reader)

fileData.pop(0)

newData = []

for i in range(len(fileData)):
    num = fileData[i][1]
    newData.append(float(num))
    
n = len(newData)

sum = 0

for i in newData:
    sum+= i 
    
mean = sum/n


print("Calculating......................................................................................................................")
print("The Mean of data is :" + str(mean))