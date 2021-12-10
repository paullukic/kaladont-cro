# Zanima nas koji je najduži niz riječi koji se može odigrati u "Kalodontu". 
# Niz može početi s bilo kojom riječi, a prva dva slova svake iduće riječi moraju biti jednaka završetku prethodne riječi. 
# Dozvoljene su sve riječi iz liste od oko 160 tisuća riječi pisanih malim slovima (a-z, znak -). 
import random
import sys
sys.setrecursionlimit(10**6)

file1 = open('words.txt', 'r')
Lines = file1.readlines()

kaladont = []
kaladonts = []

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()

def lastTwo(word):
    return word[-2:]

def firstTwo(word):
    return word[:2]

def find_max_list(lista):
    list_len = [len(i) for i in lista]
    return max(list_len)

# funckija za pronalazenje kaladonta
def findWord(word, array, counter):
    for i in range(len(array)):
        if firstTwo(array[i]) == lastTwo(word) and counter < 1:
            kaladont.append(array[i])
            starterWord = array[i];
            counter += 1

            newArray = [x for x in array if x != array[i]]
            findWord(kaladont[-1], newArray, 0)
        
        else:
            continue
count = 0
# za svaku rec u tekstu, proveravamo da li su prva dva slova jednaka zavrsetku prethodne reci.
for i in range(len(Lines)):
    # izvuci rec 
    newWord = Lines[i]

    # dodaj rec u listu kaladont
    kaladont.append(newWord)

    # izbaci rec iz liste
    Lines.remove(newWord)

    # pokreni funkciju za pronalazenje kaladonta
    findWord(newWord, Lines, 0)

    # dodaj kaladont u listu kaladonts
    kaladonts.append(kaladont)

    # ocisti kaladont listu
    kaladont = []
    count += 1
    print('Zavrsenih reci: ',count)

# pronadji index najduzeg niza
longest = find_max_list(kaladonts)

# postavi najduzi niz u varijablu
longestKaladont = kaladonts[longest]

# ispisi najduzi niz u kaladont.txt
for i in range(len(longestKaladont)):
    with open('kaladont.txt', 'a') as f:
        f.write(longestKaladont[i] + ' ')