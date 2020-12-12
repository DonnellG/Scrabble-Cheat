import pygame as pg

#Scrabble Cheat Logic
def ScrabbleCheat(text):
    #create score dictionay
    scoreKey ={"a" :1,"b" :3, "c" :3, "d" :2, "e" :1, "f" :4,
            "g" :2, "h" :4, "i" :1, "j" :8, "k" :5, "l" :1,
            "m" :3, "n" :1, "o" :1, "p" :3, "q" :10, "r" :1,
            "s" :1, "t" :1, "u" :1, "v" :4, "w" :4, "x" :8,
            "y" :4, "z" :10}

    #create list of words
    txtdoc = open(r"C:\Users\zanko\OneDrive\Programing\Python\Scrabble Cheat\sowpods.txt")
    words=[]
    for n in txtdoc:
        if len(n)<=len(text)+1:
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
        if testWord(word, text):
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

    
    #input('Hit enter to exit')
    return finalList

#Start of PyGame Stuff
words = []
#Start Game
pg.init()

#Screen Attributes 
pg.display.set_caption("Scrabble Cheat")
icon = pg.image.load('icon-ScrabbleWindow.png')
pg.display.set_icon(icon)
fontInstruc = pg.font.Font(None,32)
fontOutputTitle = pg.font.Font(None,20)
fontWordlist = pg.font.Font(None,32)

# create the screen
screen = pg.display.set_mode((500,460))

# Text Inputbox Properties
text = ''
colorFont = pg.Color(0,0,0)
fontScrabble = pg.font.Font("Scramblemixed-YEdO.ttf", 120)
scrabbleX = 215 #1-215 2-167 3-137 4-107 5-77 6-47 7-15

#Event Input Function
def InputFunc(eventType):
    pass

#game loop
running = True
while running:
    #Screen Attributes
    screen.fill((255,255,255))

    #Checking Events
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                words = ScrabbleCheat(text)
                if len(words) > 11:
                    words = words[:10]
                text = ''
            elif event.key == pg.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pg.K_SPACE:
                continue
            else:
                if len(text) >= 7:
                    text = text[:-1]
                text += event.unicode

    #rendering the GUI Stuff
    instrucText = fontInstruc.render("Input your letters (max 7): ",True, colorFont)
    screen.blit(instrucText,(0,0))
    OutputTitleText = fontOutputTitle.render("TOP 10 HIGHEST SCORING WORDS: ",True, colorFont)
    screen.blit(OutputTitleText,(140,150))
    wordX = 200
    wordY = 200
    for word in words:
        wordListText = fontWordlist.render(word,True, colorFont)
        screen.blit(wordListText ,(wordX,wordY))
        wordX += 0
        wordY += 25

    #Rendering the text in a rectangles
    textSurface = fontScrabble.render(text,True,colorFont)
    #screen.blit(textSurface, (inputBox.x+5, inputBox.y+5))
    textNum = len(text)-1
    screen.blit(textSurface, (scrabbleX-textNum*33, 50))

    #needed to play game
    pg.display.update()