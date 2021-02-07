import pygame, random

screen = pygame.display.set_mode((800,600))

#brushColours given an RGB value
white = (255, 255, 255)
black = (  0,   0,   0)
red   = (255,   0,   0)
darkGreen = (0, 100, 0)
lightGreen = (  0, 255,   0)
pink =  (255, 182, 193)
orange = (253, 106, 2)
gold = (249, 166, 2)
yellow = (255, 255, 0)
lightYellow = (255, 255, 204)
blue = (  0,  0, 255)
lightBlue = (  0, 191, 255)
purple = (138, 43, 226)
lightPurple = (123, 104, 238)
brown = (128,0,0)
tan = (210,180,140)
UI_Col = (214, 228, 249)
UI_BorderCol = (153, 160, 170)
UI_BGCol = (239, 244, 252)


#Global variables
drawOn = False
lastPos = (0, 0)    #Sets the previous position
brushColour = black #Default brush colour, to be updated
radius = 10         #Default radius for brush size, to be updated
#----------------#
#Sets the default tool states
brushOn = True      
sprayCanOn = False
fillCanOn = False
circleOn = False
squareOn = False
lineOn = False
#----------------#
clickCount = 0   #This variable ensures that the line tool does not draw over the UI.
offset1 = -10    #Default spread values for the spray can tool.
offset2 = 10  

#screen layout
screen.fill(white)

##class UIBox:
##    def __init__(self, colour, posX, posY, width, height, oldBrushCol):
##        global brushColour
##        self.brushColour = brushColour
##        self.posX = int(posX)
##        self.posY = int(posY)
##        self.width = int(width)
##        self.height = int(height)
##
##        givenBox = pygame.draw.rect(screen, colour, (posX, posY, width, height))
##
##    
##        eventGiven = pygame.event.wait()
##        mousepos = pygame.mouse.get_pos()
##        if eventGiven.type == pygame.MOUSEBUTTONDOWN:
##            if givenBox.collidepoint(mousepos):
##                
##                brushColour = colour

    

#Joins together line to look smoother
def smoothstroke(srf, brushColour, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0]+float(i)/distance*dx)
        y = int(start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, brushColour, (x, y), radius)
#Code used from https://stackoverflow.com/questions/597369/how-to-create-ms-paint-clone-with-python-and-pygame

#Spray can tool
def sprayCan(x, y, brushColour, offset1, offset2):
            for i in range (0,10):
                sprayPos = (0, 0)
                sprayPosLst = list(sprayPos)
                sprayPosLst[0] = mousex + random.randint(offset1, offset2)
                sprayPosLst[1] = mousey + random.randint(offset1, offset2)
                sprayPos = tuple(sprayPosLst)
                
                pygame.draw.circle(screen, brushColour, sprayPos, 0)

#Resets the canvas to the desire coloured
def canvasFill(colour, screen):
    screen.fill(colour)


try:
    while True:

        #Basic_UI
        UI_Border = pygame.draw.rect(screen, UI_BorderCol, (0, 0, 2160, 100))
        UI_ = pygame.draw.rect(screen, UI_Col,(0,1,2159,98))
        UI_BG = pygame.draw.rect(screen, UI_BGCol, (8, 8, 291, 74))
        
        #Thickness_Elements
        UI_thinBox = pygame.draw.rect(screen, UI_BGCol, (325, 8, 74, 25))
        UI_mediumBox = pygame.draw.rect(screen, UI_BGCol, (325, 33, 74, 25))
        UI_thickBox = pygame.draw.rect(screen, UI_BGCol, (325, 58, 74, 25))
        UI_Thin = pygame.draw.rect(screen, black, (340, 17, 46, 5))
        UI_Medium = pygame.draw.rect(screen, black, (340, 39, 46, 10))
        UI_Thick = pygame.draw.rect(screen, black, (340, 61, 46, 15))

        #brushColour_Elements
        UI_Black = pygame.draw.rect(screen, black,(12, 12, 30, 30))
        UI_White = pygame.draw.rect(screen, white, (12, 48, 30, 30))
        UI_Red = pygame.draw.rect(screen, red, (48, 12, 30, 30))
        UI_Pink = pygame.draw.rect(screen, pink, (48, 48, 30, 30))
        UI_Orange = pygame.draw.rect(screen, orange, (84, 12, 30, 30))
        UI_Gold = pygame.draw.rect(screen, gold, (84, 48, 30, 30))
        UI_Yellow = pygame.draw.rect(screen, yellow, (120, 12, 30, 30))
        UI_LYellow = pygame.draw.rect(screen, lightYellow, (120, 48, 30, 30))
        UI_DGreen = pygame.draw.rect(screen, darkGreen, (156, 12, 30, 30))
        UI_LGreen = pygame.draw.rect(screen, lightGreen, (156, 48, 30, 30))
        UI_Blue = pygame.draw.rect(screen, blue, (192, 12, 30, 30))
        UI_LBlue = pygame.draw.rect(screen, lightBlue, (192, 48, 30, 30))
        UI_Purple = pygame.draw.rect(screen, purple, (228, 12, 30, 30))
        UI_LPurple = pygame.draw.rect(screen, lightPurple, (228, 48, 30, 30))
        UI_Brown = pygame.draw.rect(screen, brown, (264, 12, 30, 30))
        UI_Tan = pygame.draw.rect(screen, tan, (264, 48, 30, 30))
        
        UI_currentColourBG = pygame.draw.rect(screen, UI_BGCol, (595, 12, 70, 70))
        UI_currentColour = pygame.draw.rect(screen, brushColour, (600, 17, 60, 60))

        #UI_Tool Elements
        UI_FillCanvas = pygame.draw.rect(screen, UI_BGCol, (410, 12, 32, 32))
        UI_PaintBrush = pygame.draw.rect(screen, UI_BGCol, (446, 12, 32, 32))
        UI_SprayCan = pygame.draw.rect(screen, UI_BGCol, (482, 12, 32, 32))
        UI_RectToolBG = pygame.draw.rect(screen, UI_BGCol, (410, 48, 32, 32))
        UI_RectTool = pygame.draw.rect(screen, black, (413, 51, 26, 26), 1)
        UI_CircleToolBG = pygame.draw.rect(screen, UI_BGCol, (446, 48, 32, 32))
        UI_CircleTool = pygame.draw.circle(screen, black, (462, 64), 15, 1)
        UI_LineToolBG = pygame.draw.rect(screen, UI_BGCol, (482, 48, 32, 32))
        UI_LineTool = pygame.draw.line(screen, black, (482, 79), (513, 49), 1)

        #UI_Tool Images
        sprayCanimg = pygame.image.load('sprayCanBG.jpg')
        paintBrushimg = pygame.image.load('paintBrush.png')
        screen.blit(paintBrushimg, (446, 12))
        screen.blit(sprayCanimg, (485, 12))
        
        
        pygame.display.update()
        mousepos = pygame.mouse.get_pos()
        eventGiven = pygame.event.wait()
        mousex = mousepos[0]
        mousey = mousepos[1]

        #UITest = UIBox(gold, 100, 100, 100, 100, brushColour)
        if eventGiven.type == pygame.MOUSEBUTTONDOWN:

            #Draws where the user first clicks
            if brushOn:
                pygame.draw.circle(screen,brushColour, eventGiven.pos, radius)
            elif sprayCanOn:
                sprayCan(mousex, mousey, brushColour, offset1, offset2)

            #Colour selector
            if UI_Red.collidepoint(mousepos):
                brushColour = red
                clickCount = 0  #Ensures that the line tool will not draw over the UI when changing colours.
            elif UI_LGreen.collidepoint(mousepos):
                brushColour = lightGreen
                clickCount = 0
            elif UI_White.collidepoint(mousepos):
                brushColour = white
                clickCount = 0
            elif UI_Black.collidepoint(mousepos):
                brushColour = black
                clickCount = 0
            elif UI_Pink.collidepoint(mousepos):
                brushColour = pink
                clickCount = 0
            elif UI_DGreen.collidepoint(mousepos):
                brushColour = darkGreen
                clickCount = 0
            elif UI_Orange.collidepoint(mousepos):
                brushColour = orange
                clickCount = 0
            elif UI_Gold.collidepoint(mousepos):
                brushColour = gold
                clickCount = 0
            elif UI_Yellow.collidepoint(mousepos):
                brushColour = yellow
                clickCount = 0
            elif UI_LYellow.collidepoint(mousepos):
                brushColour = lightYellow
                clickCount = 0
            elif UI_Blue.collidepoint(mousepos):
                brushColour = blue
                clickCount = 0
            elif UI_LBlue.collidepoint(mousepos):
                brushColour = lightBlue
                clickCount = 0
            elif UI_Purple.collidepoint(mousepos):
                brushColour = purple
                clickCount = 0
            elif UI_LPurple.collidepoint(mousepos):
                brushColour = lightPurple
                clickCount = 0
            elif UI_Brown.collidepoint(mousepos):
                brushColour = brown
                clickCount = 0
            elif UI_Tan.collidepoint(mousepos):
                brushColour = tan
                clickCount = 0

            #Thickness selector    
            if UI_thinBox.collidepoint(mousepos):
                offset1 = -5    #Offset values for the spray can tool.
                offset2 = 5
                radius = 2      #For the paintbrush, circle, square, and line tools.
                clickCount = 0
            elif UI_mediumBox.collidepoint(mousepos):
                offset1 = -10
                offset2 = 10
                radius = 6
                clickCount = 0
            elif UI_thickBox.collidepoint(mousepos):
                offset1 = -15
                offset2 = 15
                radius = 10
                clickCount = 0
                
            #Tool selector
            #Changes all states.
            if UI_FillCanvas.collidepoint(mousepos):
                sprayCanOn = False
                brushOn = False
                circleOn = False
                squareOn = False
                lineOn = False
                drawOn = False
                fillCanOn = True
                clickCount = 0
            elif UI_SprayCan.collidepoint(mousepos):
                sprayCanOn = True
                circleOn = False
                brushOn = False
                squareOn = False
                lineOn = False
                drawOn = True
                fillCanOn = False
                clickCount = 0
            elif UI_PaintBrush.collidepoint(mousepos):
                sprayCanOn = False
                brushOn = True
                circleOn = False
                squareOn = False
                lineOn = False
                drawOn = False
                fillCanOn = False
                clickCount = 0
            elif UI_CircleTool.collidepoint(mousepos):
                sprayCanOn = False
                brushOn = False
                circleOn = True
                squareOn = False
                lineOn = False
                drawOn = False
                fillCanOn = False
                clickCount = 0
            elif UI_RectTool.collidepoint(mousepos):
                sprayCanOn = False
                brushOn = False
                circleOn = False
                squareOn = True
                lineOn = False
                drawOn = False
                fillCanOn = False
                clickCount = 0
            elif UI_LineTool.collidepoint(mousepos):
                sprayCanOn = False
                brushOn = False
                circleOn = False
                squareOn = False
                lineOn = True
                drawOn = False
                fillCanOn = False
                clickCount = 0
            else:
                drawOn = True


            #Tool functionality    
            if squareOn:
                drawOn = False
                #Draws a square in the position of the user's cursor.
                pygame.draw.rect(screen, brushColour, ((mousepos[0]-30), (mousepos[1]-30), 60, 60), radius)
            elif circleOn:
                drawOn = False
                #Draws a circle in the position of the user's cursor.
                pygame.draw.circle(screen, brushColour, (mousepos), 40, radius)
            elif lineOn:
                #Draws a line based on two clicks from the user, start position being the first click
                #and end position being the second click.
                drawOn = False
                clickCount += 1
                if clickCount == 2:
                    click1 = mousepos
                elif clickCount == 3:
                    clickCount = 1
                    click2 = mousepos
                    pygame.draw.line(screen, brushColour, click1, click2, radius)
            elif lineOn == False:
                clickCount = 0

            if fillCanOn and drawOn:
                #Calls the canvas fill function
                canvasFill(brushColour, screen)

                
        if eventGiven.type == pygame.MOUSEBUTTONUP:
            drawOn = False
            #Stops drawing
            
        elif eventGiven.type == pygame.MOUSEMOTION:
            if drawOn and sprayCanOn == False:
                #Draws a smooth line when the mouse is movied.
                pygame.draw.circle(screen, brushColour, eventGiven.pos, radius)
                smoothstroke(screen, brushColour, eventGiven.pos, lastPos,  radius)
                
            if drawOn and sprayCanOn:
                sprayCan(mousex, mousey, brushColour, offset1, offset2)
                
            lastPos = eventGiven.pos
        pygame.display.flip()

        if eventGiven.type == pygame.QUIT:
            raise StopIteration
            #Quits the program when the red X is pressed.
        
except StopIteration:
    pass

pygame.quit()
