#create score dictionay
scoreKey ={"a" :1,"b" :3, "c" :3, "d" :2, "e" :1, "f" :4,
         "g" :2, "h" :4, "i" :1, "j" :8, "k" :5, "l" :1,
         "m" :3, "n" :1, "o" :1, "p" :3, "q" :10, "r" :1,
         "s" :1, "t" :1, "u" :1, "v" :4, "w" :4, "x" :8,
         "y" :4, "z" :10}

#Ask user for Letters
rack = input("Enter your rack letters: ").lower()

#create list of words
txtdoc = open(r"C:\Users\zanko\OneDrive\Programing\Python\Scrabble Cheat\sowpods.txt")
words=[]
for n in txtdoc:
    if len(n)<=len(rack)+1:
        words.append(n[:-1].lower())

# search for the valid words
validWords = []

def testWord(word,testrack):
    for l in word:
        if testrack.find(l) != -1:
            lindex = testrack.find(l)
            testrack = testrack[0:lindex]+testrack[lindex+1:]
        else:
            return False
    return True

for word in words:
    if testWord(word, rack):
        validWords.append(word)

#Score words
def wordScore(word):
    score = 0
    for i in word:
        score += scoreKey[i]
    return score

validWordDic = []
scores = []
for word in validWords:
    word_score = wordScore(word)
    validWordDic.append(str(word_score) + ' ' + word)
    scores.append(word_score)

#print score + word
sortedScores = scores.copy()
sortedScores.sort(reverse = True)
finalList = []

for i in sortedScores:
    scoreIndex = scores.index(i)
    finalList.append(validWordDic[scoreIndex])
    scores[scoreIndex]='XXXX'

for i in finalList:
    print(i)


input('Hit enter to exit')
