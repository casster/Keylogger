import re
import matplotlib.pyplot as plt
import numpy as np
import operator

class KeyTime:

    def __init__(self,time,key):
        self.__key = key
        self.__time = time
    
    def getKey(self):
        return self.__key
    
    def setKey(self,key):
        self.__key = key

    def getTime(self):
        return self.__time

    def setTime(self,time):
        self.__time = time


textFile  = open("keyLog.txt", "r")

items = []
for line in textFile:
    time = line[11:23]
    if line[25] == "'":
        key = line[26]
    elif line[25] == 'K':
        key = line[29:]
        key = re.sub('\n','',key) #removes the newline char
    elif line[25] == 'B':
        key = line[32:]
        key = re.sub('\n','',key)
    items.append(KeyTime(time,key))


textFile.close()

freq = {} #creating frequency dictionary
for item in items:
    if item.getKey() in freq:
        freq[item.getKey()] += 1
    else:
        freq[item.getKey()] = 1

textFile = open("results.txt","w") #outputting dictionary as a textfile
for k,v in freq.items():
    line = ''
    line = line + k + " : " + str(v) + "\n"
    textFile.write(line)
textFile.close()

sortedFreq = sorted(freq.items(), key=operator.itemgetter(1)) #sorts the dictionary

keyAxis = [""]
freqAxis = [0] #creating the axis list for the bar chart
for item in sortedFreq:
    keyAxis.append(item[0])
    freqAxis.append(item[1])

xAxis = np.arange(len(keyAxis))
plt.figure(figsize=(13,5))
plt.bar(xAxis,freqAxis, align = 'center',color='blue',edgecolor='black',width=1)
plt.xticks(xAxis, keyAxis)
plt.xlabel('Key', fontsize=16)
plt.ylabel('Num. times pressed', fontsize=16)
plt.title('Bar chart of my keys pressed',fontsize=20)
plt.show()
