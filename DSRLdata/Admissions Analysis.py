# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 18:58:24 2019

@author: Nadia
"""
import csv
import statistics
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
columns = defaultdict(list)
with open('HYPSMadmission.csv') as admissions:
    csv_reader = csv.reader(admissions, delimiter=',')
    line_count=0
    for row in csv_reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)

years = columns[0]
harv = columns[1]
yale = columns[2]
prince = columns[3]
stan = columns[4]
mit = columns[5]

harv1 = [float(n) for n in harv[1:]]
yale1 = [float(n) for n in yale[1:]]
prince1 = [float(n) for n in prince[1:]]
stan1 = [float(n) for n in stan[1:]]
mit1 = [float(n) for n in mit[1:]]

plt.plot(years[1:],harv1,label="Harvard", color="crimson")
plt.plot(years[1:],yale1,label="Yale",color="navy")
plt.plot(years[1:],prince1,label="Princeton",color="orange")
plt.plot(years[1:],stan1,label="Stanford",color="maroon")
plt.plot(years[1:],mit1,label="MIT",color="gray")
plt.title('Number of Admitted Students Per Year by University 2010-2018')
plt.xlabel('Year')
plt.ylabel('Students')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

hsd = statistics.stdev(harv1)
ysd = statistics.stdev(yale1)
psd = statistics.stdev(prince1)
ssd = statistics.stdev(stan1)
msd = statistics.stdev(mit1)
labels = ["Harvard", "Yale", "Princeton", "Stanford", "MIT"]
index = np.arange(len(labels))
SD1 = [hsd,ysd,psd,ssd,msd]

plt.bar(index,SD1, color = ("crimson", "navy", "orange", "maroon", "gray"))
plt.title('Standard Deviation of Admitted Students Per Year by University 2010-2018')
plt.xlabel('School')
plt.xticks(index,labels)
plt.ylabel('Standard Deviation')
for a, b in zip(index, SD1):
    plt.text(a, b, round(b))
plt.show()