import csv
from datetime import date
import numpy as np
import matplotlib.pyplot as plt



startDate = date(2015,6,19)
authors = []
dateY = []
filenames = []
edits = {}
with open('authorDate.csv','r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file, delimiter=",")
    for line in csv_dict_reader:
        authors.append(line['Author Name'])
        filenames.append(line['Filename'])
        dateY.append(int((date(int(line['Date'][0:4]),int(line['Date'][5:7]),int(line['Date'][8:10]))-startDate).days/7))
csv_file.close()

fileNumX = []
auths = {}
authColor = []
for currFile, currAuth in zip(filenames,authors):
    needToAdd = True
    newID = 0
    for ind,currEdit in enumerate(edits):
        if (currFile.find(currEdit) > -1):
            fileNumX.append(ind)
            needToAdd = False
        else:
            newID = ind+1
    if(needToAdd):
        fileNumX.append(newID)
        edits[currFile] = []
    needToAdd = True
    newID = 0
    for ind,currCol in enumerate(auths):
        if (currAuth.find(currCol) > -1):
            authColor.append(ind*100)
            needToAdd = False
        else:
            newID = ind+1
    if(needToAdd):
        authColor.append(newID*100)
        auths[currAuth] = []

plt.title('scottyab/rootbeer changes')
plt.xlabel('File')
plt.ylabel('Weeks')
plt.scatter(fileNumX, dateY, c=authColor, cmap = 'plasma', s=100)

plt.show()
