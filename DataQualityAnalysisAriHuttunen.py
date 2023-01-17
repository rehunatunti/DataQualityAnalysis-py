#Kommentin kirjoittajan tiedot
# Ari Huttunen
# 10.11.2022

#InputFilePath = "Test.txt"
InputFilePath = "DataQualityInput.txt"

#Tiedoston avaaminen lukemista varten
# Ei tehdä virheentarkistusta, onko tiedosto olemassa vai ei - - tämä hyvä mainita
ifh = open(InputFilePath, "r") 	# input file handler, avaus-metodi, 
								#jonka parametreina on tiedostopolku ja lukutoiminto ("r")
# Listan alustus
List = []
for line in ifh: 	# Luetaan rivi kerrallaan
    if line == "\n":
    	List.append(None) 	# lisätään Null-arvo
    else:
    	List.append(int(line))	# otetaan rivinvaihto pois, 
    							# ennen kuin lisätään ja muutetaan int:ksi
print(List) 
# Muuttujien alustus:
Total = len(List) # len(): listan alkioiden määrä, joka sijoitetaan Total-muuttujaan
Null = 0 
NonNull = 0
Duplicate = 0
Distinct = 0
NonUnique = 0
Unique = 0
# Käydään lista läpi alkio kerrallaan ja etsitään None eli Null-arvot
for l in List:
	if l == None: 
		Null = Null + 1 # Null-muuttujaan lisätään 1
		List.remove(l)	# listasta poistetaan yksi alkio

#Muuttujiin sijoituksia ja laskutoimituksia
NonNull = Total - Null 	# Totalista poistetaan Null-muuttujan arvon verran kokonaislukuja,
						# saadaan ei-nolla-arvojen määrä
Set = set(List) 		# Lyhyesti: Listasta tehdään set, jotta listasta poistetaan duplikaatit
						# ((set()-metodi tekee listan alkioista joukon ja joukko sijoitetaan
						# Set-muuttujaan. Joukossa on lueteltu eri arvoja sisältävät alkiot.))
Distinct = len(Set) 	# Joukon alkioiden määrä saadaan len()-metodilla, eli kuinka monta 
						# arvoa on distinct, (diskreetti arvo?), erilaiset arvot
Duplicate = NonNull - Distinct	# Duplicate-muuttujaan sijoitetaan ei-nollien ja distinct arvojen erotus

# Käydään lista läpi uniikkien alkioiden selvittämiseksi
for x in List:			
	if List.count(x) == 1:	# count(x) metodi kertoo jonkin tietyn alkion lukumäärän 
							# listassa 
		Unique = Unique + 1 # Joka kerta kun jonkin alkion count on 1, Unique-muuttujan 
							# määrä kasvaa
NonUnique = Distinct - Unique 	# distinct arvojen määrästä vähennetään uniikkien arvojen määrä

# Tuloksen esitysmuodon formatointia
# Ennakoivaa koodaamista, esim. seuraavan koodaajan helppo muokata formaattia haluamakseen
DQA= "Data Quality Analysis"
T = "Total"
N = "  Null"
Nn = "  NonNull"
Dup = "    Duplicate"
Dis = "    Distinct"
Nunq = "      NonUnique"
Unq = "      Unique"

print()
""" 
Tulosten tulostaminen formatointia käyttäen
f = format, teksti tasataan vasemmalle (oletus), 
luku tasataan oikealle (oletus) 
> = tasaus oikealle, < = tasaus vasemmalle, ^ = tasaus keskelle, d = int, f = float
5d = varataan 5 paikkaa luvulle
{} = itsenäinen blokki
: = erotin
'Count' on string, literaali teksti
"""
print(f"{DQA:10}\t{'Count':>5}\t{'%':>5}")	
print(f"{T:10}\t\t{Total:5d}\t{(Total/Total)*100:5.0f}")
print(f"{N:10}\t\t{Null:5d}\t{(Null/Total)*100:5.0f}")
print(f"{Nn:10}\t\t{NonNull:5d}\t{(NonNull/Total)*100:5.0f}")
print(f"{Dup:10}\t\t{Duplicate:7d}\t{(Duplicate/Total)*100:7.0f}")
print(f"{Dis:10}\t\t{Distinct:7d}\t{(Distinct/Total)*100:7.0f}")
print(f"{Nunq:10}\t\t{NonUnique:9d}{(NonUnique/Total)*100:9.0f}")
print(f"{Unq:10}\t\t{Unique:9d}{(Unique/Total)*100:9.0f}")
print()
