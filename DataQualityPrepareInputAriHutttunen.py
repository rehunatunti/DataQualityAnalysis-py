#Kommentin kirjoittajan tiedot
# Ari Huttunen
# 10.11.2022

# Random-moduulin käyttöönotto, random-kokonaislukuja
from random import random, randint
  
# Listan alustus
RandomList = []

# For-luupin ja laskurimuuttuja i:n (0-99) avulla arvotaan 100 kertaa kokonaisluku 
# -20 ja 25 väliltä.
for i in range(100):
  r = randint(-20,25) # randint() palauttaa kokonaisluvun -20 ja 25 väliltä, 
                      # sisältäen molemmat luvut
  if r > 20:  # lisäehto, että luku saa olla korkeintaan 20.
    RandomList.append(None) #Listaan lisätään tyhjä, null-arvo jos arvottu luku on 
                            #isompi kuin 20.
  else:
    RandomList.append(r) # Muussa tapauksessa jokainen uusi arvottu luku lisätään listan loppuun.
    
print(RandomList)

# tulostustiedoston avaus
# Ei virheentarkistusta, onko tiedosto olemassa vai ei.
OutputFilePath = "DataQualityInput.txt"

ofh = open(OutputFilePath, "w") # output file handler muuttuja, avaus-metodi jonka parametreiksi tiedostopolku ja "w" write-toiminto
# Käydään listan jokainen luku läpi n avulla
for n in RandomList:
  if n == None:
    ofh.write("\n") # Jos jokin listan alkio on nolla-arvo, tiedostoon tulostetaan riviväli
  else:
    ofh.write(str(n) + "\n") # muussa tapauksessa kirjoitetaan rivi ja lisätään rivinvaihto
ofh.close # suljetaan tiedosto
print("Done")