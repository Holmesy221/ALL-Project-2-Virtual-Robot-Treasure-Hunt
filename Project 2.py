from Tkinter import *
import time
import random
from math import sqrt

window = Tk()
canvas = Canvas(window, width=1500, height=750, bg='white')
canvas.pack()
canvas.pack(padx=10,pady=10)

Randomx = random.randint(1,6) #The initial starting speeds of both robots.
Randomy = random.randint(2,6)

vx = Randomx
vy = Randomy

x_min = 0.0     #The boundarys of the screen.
y_min = 0.0
x_max = 1500
y_max = 750.0
     
rec = [[0,0,2,751,],[0,0,1500,2],           #The coordinates of every rectangle drawn on screen.
       [1500,0,1502,751],[0,751,1500,751],
       [0,0,21,83],[133,0,194,110],
       [194, 0,350,20],[350,0,427,110],
       [0,164,20,552],[245,60,290,130],
       [136,413,414,467],[0,630,22,751],
       [22,730,896,751],[278,467,316,654],
       [136,467,178,503],[136,569,178,655],
       [470,413,594,467],[517,467,594,655],
       [402,610,517,655],[300,320,594,369],
       [420,270,594,320],[360,520,460,565],
       [138,225,345,271],[20,320,225,369],
       [594,610,760,655],[645,413,760,565],
       [645,270,900,369],[427,0,900,20],
       [475,75,594,215],[594,75,700,100],
       [775,75,900,100],[594,190,775,215],
       [845,100,900,215],[635,135,845,160],
       [810,413,900,510],[810,555,900,655],
       [955,413,1045,470],[955,595,1045,655],
       [955,180,1045,369],[955,0,1045,115],
       [1045,620,1190,655],[1045,413,1190,448],
       [1075,517,1260,547],[1260,480,1290,594],
       [1100,0,1130,100],[1100,150,1130,300],
       [1100,339,1345,369],[1400,339,1500,369],
       [1170,40,1460,70],[1240,110,1390,140],
       [1170,180,1460,210],[1170,210,1200,300],
       [1240,270,1460,300],[1345,413,1400,655],
       [980,730,1500,751],[1480,369,1500,730]]

TLight = [[585,215,588,270],[651,215,654,270], #The Coordinates of every Light Door on the screen.
          [594,146,635,149],[154,503,157,569],
          [178,640,278,643],[316,640,402,643],
          [414,425,470,427],[225,342,300,345],
          [855,655,858,730],[1147,448,1150,517],
          [1147,547,1150,620],[999,115,1002,180],
          [1314,70,1317,110],[1314,140,1317,180],
          [1345,353,1400,356],[0,0,0,0]]

TLights = []

for s in range (0,len(TLight)):
    TLights.append([canvas.create_rectangle(TLight[s], outline= 'Black'),0])
    
for s in range (0,len(rec)):
    Square1 =canvas.create_rectangle(rec[s], outline= 'black')

    #l = Label(text=rec[s])
    #l.place(x = rec[s][0],y = rec[s][1])   #Labels with coordinates place
                                              #to help when designing the map.

AmountofRobots = input(["Enter the amount of Robots you wish to see"])

AmountofRobots = int(AmountofRobots)

Robots = []

for r in range (0,AmountofRobots):
    RandomX = random.randint(40,1460)
    RandomY = random.randint(40,710)
    Robots.append([canvas.create_rectangle(RandomX,RandomY,RandomX + 10,RandomY + 10,outline ='Black', fill = 'Light Blue'),vx,vy])


def ChangeTLights():
    for l in range (0,len(TLights)): #This is used to randomly change the colour of the lights throughout the map.
        RandomVal = random.randint(0,1000) #Random value between 0 and 1000
        if RandomVal > 60 and RandomVal < 70: #If the value is between 60 and 70 the is true. 
            if TLights[l][1] == 0: #Secondary value in list used to mark whether the light is currently, 
                canvas.itemconfig(TLights[l][0],fill = 'Red',outline = 'Red') #Red or Green. 0 = Green. 1= Red.
                TLights[l][1] = 1                 
            else:
                canvas.itemconfig(TLights[l][0],fill = 'Green',outline = 'Green')
                TLights[l][1] = 0
                
def CollisonDetection(x1,y1,x2,y2,vx,vy):

    for R in range (0,len(rec)): #Checking colliosion detection between the robot and all 56 walls on screen.

        if x2>(rec[R][0] - 13) and x2<(rec[R][0] + 13) and y1< rec[R][3] and y1>rec[R][1]: #left side. 
            vx = vx -3.0 
        
        if x1>(rec[R][2] - 13) and x1<(rec[R][2] + 13) and y1< rec[R][3] and y1>rec[R][1]: #right side.
            vx = vx +3.0
        
        if y2>(rec[R][1] - 13) and y2<(rec[R][1]+13) and x1>rec[R][0] and x1<rec[R][2]: #Top
            vy = vy - 3.0
        
        if y1>(rec[R][3] - 13) and y1<(rec[R][3]+13) and x1>rec[R][0] and x1<rec[R][2]: #Bottom
            vy = vy + 3.0

    for L in range (0,len(TLight)):  #Check for collision between Robot and Red Lights.
      
        if x2>(TLight[L][0] - 13) and x2<(TLight[L][0] + 13) and y1< TLight[L][3] and y1>TLight[L][1] and TLights[L][1] == 1: #Right side. 
            vx = vx -3.0
                       
        if x1>(TLight[L][2] - 13) and x1<(TLight[L][2] + 13) and y1< TLight[L][3] and y1>TLight[L][1] and TLights[L][1] == 1: #Left side.
            vx = vx +3.0
          
        if y2>(TLight[L][1] - 13) and y2<(TLight[L][1]+13) and x1>TLight[L][0] and x1<TLight[L][2] and TLights[L][1] == 1: #Top
            vy = vy - 3.0
        
        if y1>(TLight[L][3] - 13) and y1<(TLight[L][3]+13)and x1>TLight[L][0] and x1<TLight[L][2] and TLights[L][1] == 1: #Bottom
            vy = vy + 3.0

    return vx,vy;
            
def CheckMaxSpeed(vx,vy):
    if vx > 6: #If the speed of the Robot ever exeeds 6 or -6,
        vx = 6  #the robot is limited to the max speed of 6. 
    if vx <-6:
        vx = -6
    if vy > 6:
        vy = 6
    if vy < -6:
        vy = -6       

    if vx == 0: #Stops the robot from ever having a verticle or horizontal speed of 0. 
        vx = 1
    if vy == 0:
        vy = 1

    return vx,vy;

def CheckBoundarys(x1,y1,x2,y2,vx,vy):
    
    if x2 >= x_max: #Keeps the robot within the boundarys of the Map. 
        vx = -vx
    if y1 <= y_min:
        vy = -vy
    if y2 >= y_max:
        vy = -vy
    if x1 <= x_min:
        vx = -vx

    return vx,vy;

     

def GetDistance(x1,y1,x2,y2,vx,vy):

    distances = []
    
    for x in range (0,int((len(Robots)))):
        
        rx1,ry1,rx2,ry2= canvas.coords(Robots[x][0])
        
        rvx = Robots[x][1]
        rvy = Robots[x][2]

        if x1 == rx1:
            continue
        else:
            p1 = [x2-5,y2-5]
            p2 = [rx2-5,ry2-5]
            distances.append(sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))
         
    return distances;

def AvoidRobots(x1,y1,x2,y2,vx,vy):

    distances = GetDistance(x1,y1,x2,y2,vx,vy)

    for x in range (0,int(AmountofRobots/2)):
        if distances[x] < 40:
            vx = -vx
            vy = -vy
                  
    return vx,vy;

#-----------------------------------------------------------------------------------------------

for t in range(1, 1000000): #Main loop to run the program.

    ChangeTLights()
    
    for x in range (0,AmountofRobots):

        vx = Robots[x][1]
        vy = Robots[x][2]
            
        x1,y1,x2,y2 = canvas.coords(Robots[x][0]) #Retrieves and stores the coordinates of the Robot.
               
        vx,vy = CollisonDetection(x1,y1,x2,y2,vx,vy)

        vx,vy = CheckMaxSpeed(vx,vy)

        vx,vy = CheckBoundarys(x1,y1,x2,y2,vx,vy)

        #vx, vy = AvoidRobots(x1,y1,x2,y2,vx,vy)

        Robots[x][1] = vx
        Robots[x][2] = vy
        
        canvas.coords(Robots[x][0],x1+vx,y1+vy,x2+vx,y2+vy)

                                      
#-----------------------------------------------------------------------------------------------
            
    canvas.update()
    time.sleep(0.05)
window.mainloop()

