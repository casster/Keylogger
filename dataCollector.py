import re
import matplotlib.pyplot as plt
import numpy as np

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
    else:
        key = line[25:]
        key = re.sub('\n','',key) #removes the newline char
    items.append(KeyTime(time,key))


textFile.close()

freq = {}
for item in items:
    if item.getKey() in freq:
        freq[item.getKey()] += 1
    else:
        freq[item.getKey()] = 1

keyAxis = [] #x
freqAxis = [] #y
textFile = open("results.txt","w")
for k,v in freq.items():
    keyAxis.append(k)
    freqAxis.append(str(v))
    line = ''
    line = line + k + " : " + str(v) + "\n"
    textFile.write(line)
textFile.close()

xAxis = np.arange(len(keyAxis))
plt.bar(xAxis,freqAxis,color='blue',edgecolor='black')
plt.xticks(xAxis, keyAxis)
plt.xlabel('Key', fontsize=16)
plt.ylabel('Num. times pressed', fontsize=16)
plt.title('Bar chart of my keys pressed',fontsize=20)
plt.show()
