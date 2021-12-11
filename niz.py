# Zanima nas koji je najduži niz riječi koji se može odigrati u "Kalodontu". 
# Niz može početi s bilo kojom riječi, a prva dva slova svake iduće riječi moraju biti jednaka završetku prethodne riječi. 
# Dozvoljene su sve riječi iz liste od oko 160 tisuća riječi pisanih malim slovima (a-z, znak -). 
import sys
import os
import threading
import time

sys.setrecursionlimit(10**6)

file1 = open('words.txt', 'r')
Lines = file1.readlines()
for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()

# kopiranje niza koji ce se menjati tokom rekurzije i threadova
copyLines = Lines.copy()
kaladonts = {}

class allKaladonts:
    def __init__(self, firstWord, kaladont=None):
        self.firstWord = firstWord
        self.kaladont = kaladont or []

def lastTwo(word):
    return word[-2:]

def firstTwo(word):
    return word[:2]

def find_max_list(lista):
    list_len = [len(i) for i in lista]
    return max(list_len)

# rekurzija za pronalazenje kaladonta
def findWord(word, array, counter, firstWord):
    words = array.copy()
    for i in range(len(words)):
        if firstTwo(words[i]) == lastTwo(word) and counter < 1:
            counter += 1
            kaladonts[firstWord].kaladont.append(words[i])
            filteredWords = [x for x in words if x != words[i]]
            findWord(words[i], filteredWords, 0, firstWord)
        else:
            continue
# iz svih kaladonta izvuci najduzi niz
def getLongestList(kaladonts):
    # pronadji index najduzeg niza
    listKal = [i.kaladont for i in kaladonts]

    longest = find_max_list(listKal)

    # postavi najduzi niz u varijablu
    longestKaladont = listKal[longest]

    # ispisi najduzi niz u kaladont.txt
    for i in range(len(longestKaladont)):
        with open('kaladont.txt', 'a') as f:
            f.write(longestKaladont[i] + ' ')

# za svaku rec u tekstu, proveravamo da li su prva dva slova jednaka zavrsetku prethodne reci.
def main(Lines, threadCounter, kaladonts):

    for i in range(len(Lines)):
        # ako ne postoji vise reci u nizu inicijalnih reci pronadji najduzi niz
        if(len(copyLines) < 1):
            getLongestList(kaladonts)
            break

        else:
            # izvuci rec 
            word = copyLines[0]
            copyLines.remove(word)
            print('Thread: ' + str(threadCounter) + ' - ' + word)

            kaladonts[word] = allKaladonts(word, [])
            
            # pokreni funkciju za pronalazenje kaladonta
            findWord(word, Lines, 0, word)

            print('Thread: ' + str(threadCounter) + ' - ' + word + ' - done')
            print('Kaladont: ', kaladonts[word].kaladont)


    time.sleep(1)


for i in range(os.cpu_count()):
    thread = threading.Thread(target=main, args=(Lines, i, kaladonts))
    thread.start()
    