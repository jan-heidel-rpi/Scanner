import os
import csv
mac ='44:4E:6D'
with open('vendor.csv','r')as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for line in reader:
        if reader == mac:
            print('found')
            break
        else:
            print('not')
