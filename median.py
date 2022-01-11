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

newData.sort()

if n%2 == 0:
    m1 = newData[n//2]
    m2 = newData[n//2 - 1]
    m = (m1+m2)/2

else:
    m = newData[n//2]
    print(n)

print("Calculating......................................................................................................................")
print("The Median pf data is :" + str(m))