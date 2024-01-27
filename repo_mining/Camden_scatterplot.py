import csv
from datetime import date
#import numpy as np
#import matplotlib.pyplot as plt

startDate = date(2015,6,19)
authors = []
dates = []
filenames = []
edits = {}
with open('authorDate.csv','r') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file, delimiter=",")
    for line in csv_dict_reader:
        authors.append(line['Author Name'])
        filenames.append(line['Filename'])
        dates.append(int((date(int(line['Date'][0:4]),int(line['Date'][5:7]),int(line['Date'][8:10]))-startDate).days/7))
csv_file.close()

for (currFile,currAuth,currDate) in zip(filenames,authors,dates):
    needToAdd = True
    for currEdit in edits:
        if (currFile.find(currEdit) > -1):
            edits[currFile].append(currAuth)
            edits[currFile].append(currDate)
            needToAdd = False
    if(needToAdd):
        edits[currFile] = [currAuth,currDate]


for currEdit in edits:
    print("This is the file: " + str(currEdit))
    for ind,curr in enumerate(edits[currEdit]):
        if(ind % 2 == 0):
           print("This is the Author: " + str(edits[currEdit][ind]))
        else:
            print("This is the Date: " + str(edits[currEdit][ind]))

    