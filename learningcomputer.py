


#Reads text file
lines = []
source = open('tweets','r')
for line in source:
    lines.append(line)
source.close()

codex = {}

linetest = []

for r in lines[:5]
    row = r.split()[:-3]
    linetest.append(row)

for n in range len(linetest):
    for i in range(len(linetest[n])):
        if i in codex:
            #If in dictionary, check to see if word is in key    
        else: 
            #If not in dictionary, add it with next word
            codex[i] = i+1            
