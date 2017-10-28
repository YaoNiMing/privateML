#Import libraries
import csv
from dateutil import parser as psr
import matplotlib.pyplot as plt
import numpy as np

times_dict = {}
counts_dict = {}

def splitvalues(dictionary, key):
    date_vector = []
    count_vector = []
    for value in dictionary[key]:
        date_vector.append(value[0])
        count_vector.append(value[1])
    return date_vector, count_vector

for fileno in range(4):#This iterates through all 4 files
    #Open a data file and read it into the dictionary
    with open('turnstile'+str(fileno+1)+'.txt','r') as filecsv:
        datadict = {};
        dataset = csv.reader(filecsv, dialect='excel')
        for line in dataset:
            strippedline= map(str.strip, line)
            key = tuple(strippedline[0:3])
            values = strippedline[3:]
            for i in range(len(values)):
                #the data rolls over after every 5th entry
                if (i % 5 == 0):
                    if (key not in datadict):
                        datadict[key] = []
                    if values[i+1][-5:] == '00:00':
                        time = psr.parse(values[i] + '-' + values[i+1])
                        datadict[key].append((time, values[i+4]))
            
    for key in datadict:
        times, counts = splitvalues(datadict, key)
        if key[0] not in times_dict:
            times_dict[key[0]] = []
            counts_dict[key[0]] = []
        exits_last_hour = list(np.diff(map(int, counts)))
        if times_dict[key[0]] != [] and times != []:
            if times[0] > times_dict[key[0]][-1]: #check if new week
                times_dict[key[0]] += times[1:]
                counts_dict[key[0]] += exits_last_hour
            else: #add turnstile exit data to control area total
                num_entries = min(len(exits_last_hour),\
                    len(counts_dict[key[0]][-len(exits_last_hour):]))
                if num_entries:
                    array1 = np.array(counts_dict[key[0]][-num_entries:])
                    array2 = np.array(exits_last_hour[-num_entries:])
                    counts_dict[key[0]][-num_entries:] = list(array1+array2)
        elif times != []:
            times_dict[key[0]] += times[1:]
            counts_dict[key[0]] += exits_last_hour
#plot time series for control zone A002        
plt.plot(times_dict['A002'],counts_dict['A002'])