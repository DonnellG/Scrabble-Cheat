import pygame as pg


#Start Game
pg.init()



#Screen Attributes 
pg.display.set_caption("Input Text on Screen Testing")
icon = pg.image.load('icon-ScrabbleWindow.png')
pg.display.set_icon(icon)

# create the screen
screen = pg.display.set_mode((500,200))

# Text Inputbox Properties
text = ''
colorFont = pg.Color(0,0,0)
colorRect = pg.Color(255,255,255)
font = pg.font.Font("Scramblemixed-YEdO.ttf",120)
inputBox = pg.Rect(10,40,200,120)

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
                print (text)
                text = ''
            elif event.key == pg.K_BACKSPACE:
                text = text[:-1]
            else:
                if len(text) >= 7:
                    text = text[:-1]
                text += event.unicode

    #Rendering the text in a rectangles
    textSurface = font.render(text,True,colorFont)
    screen.blit(textSurface, (inputBox.x+5, inputBox.y+5))
    pg.draw.rect(screen, colorRect, inputBox, 2)
    #pg.display.flip()

    #needed to play game
    pg.display.update()