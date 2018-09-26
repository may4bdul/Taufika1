import math, numpy, random #handy system and math functions
from psychopy import core, event, visual, gui #these are the psychopy modules

myWin = visual.Window(color='tan', units='pix', size=[800,800], allowGUI=False, fullscr=False)#creates a window 
myClock = core.Clock() #this creates and starts a clock which we can later read

movingSquare = visual.Rect(myWin, width=200, height=200, fillColor='peachpuff', lineColor=[90,1,1])
occludingSquare = visual.Rect(myWin, width=100, height=200, fillColor='blueviolet', lineColor=[1.0,-1,-1])

myScale = visual.RatingScale(myWin, pos=[0, -360], low=100, high=180,  textSize=10, lineColor='red',  tickHeight=False, scale=None, showAccept=False, singleClick=True)
information=visual.TextStim(myWin, pos=[0,-385], text='', height=18, color='black') 
title=visual.TextStim(myWin, pos=[0,305], text='Breathing Square Illusion', height=35, color='lightcyan', italic=True, bold=True, font='forte') 

# draw four occluders at a distance 'distance'
def drawOccluders(distance= 120): 

    for xposition in [distance,-distance]:
        for yposition in [distance,-distance]:
            occludingSquare.setPos([xposition,yposition])
            occludingSquare.draw()

# the main loop
def mainLoop(distanceOfOccluders =120):
    
    finished = False

    while not finished:
        
        movingSquare.draw()
        movingSquare.setOri(2, operation="+")
        drawOccluders(distanceOfOccluders)
        
        title.draw()
        information.draw()
        myScale.draw()
        myWin.flip()

        if movingSquare.ori >= 360: 
            movingSquare.ori =0
        
        if myScale.noResponse ==False: #some new value has been selected with the mouse
            distanceOfOccluders = myScale.getRating()
            information.setText(str(distanceOfOccluders))
            myScale.reset()
    
        if event.getKeys(keyList=['escape']): 
            finished =True
    
        waitUntil = myClock.getTime() + 1 / 60.   # one second divided by 60 (most monitors are 60Hz), which is 0.016..
        while myClock.getTime() <waitUntil:
            pass
    
mainLoop() #enters the main loop
myWin.close() #closes the window
core.quit() #quits





