
import csv
from pandas import *
#import random

nodes = {}
class_0 = {}
edges = []


with open('allNodes.csv', newline='') as grossFile:
    spamreader = csv.reader(grossFile, delimiter=',', quotechar='|')
    next(spamreader)
    for row in spamreader:
        if(int(row[0]) not in nodes):
            nodes[int(row[0])] = '-'.join([str(item) for item in row[1:]])
        
        
    
grossFile.close()

  
with open('nodes+modularityClass.csv', newline='') as nodeClassesFile:
    spamreader = csv.reader(nodeClassesFile, delimiter=',', quotechar='|')
    next(spamreader)
    for row in spamreader:
        if(int(row[3]) == 3):
            if(int(row[0]) not in class_0):
                class_0[int(row[0])] = nodes[int(row[0])]
    
nodeClassesFile.close()


with open('diverseEdges.csv', newline='') as grossFile:
    spamreader = csv.reader(grossFile, delimiter=',', quotechar='|')
    next(spamreader)
    for row in spamreader:
        #print(row)
        if(int(row[0]) not in class_0):
            continue
        if(int(row[1]) not in class_0):
            continue
        if((int(row[2]) > 0 and int(row[2]) < 3 and float(row[3]) > 0.5) or (int(row[2]) >= 3 and float(row[3]) > 0.35)):
            edges.append([int(row[0]), int(row[1]), "Directed", float(row[3])])
    
grossFile.close()
print(len(edges))   

with open('class_3_edges.csv', 'w', newline='') as resEdgeFile:
    spamwriter = csv.writer(resEdgeFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Source', 'Target', 'Type', 'Weight'])
    for item in edges:
        spamwriter.writerow([item[0], item[1], item[2], item[3]])

resEdgeFile.close()

print("done with writing")