#Kommentin kirjoittajan tiedot
#etu- ja sukunimi
# PVM

from random import random, randint
  
RandomList = []
 
for i in range(100):
  r = randint(-20,25)
  if r > 20:
    RandomList.append(None)
  else:
    RandomList.append(r)
    
print(RandomList)

OutputFilePath = "DataQualityInput.txt"

ofh = open(OutputFilePath, "w")
for n in RandomList:
  if n == None:
    ofh.write("\n")
  else:
    ofh.write(str(n) + "\n")
ofh.close
print("Done")
