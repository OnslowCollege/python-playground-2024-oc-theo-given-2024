"""
Main.

Created by: Theo
Date: 24 June 2024
"""
#Setting variables
totalwindowarea = 0.0
wall1width = -1.0
wall2width = -1.0
wallsheight = -1.0
windowwidth = -1.0
windowheight = -1.0
doorsnum = -1
windowsnum = -1
#Asking for width of Wall 1
print("All values must be a number greater than zero.")
while wall1width <=0 :
    try:
        wall1width = float(input("Enter width of wall 1 (m): "))
    except ValueError:
        print ("Invalid Value")
#Asking for width of Wall 2
while wall2width <=0 :
    try:
        wall2width = float(input("Enter width of wall 2 (m): "))
    except ValueError:
        print("Invalid Value")
#Asking for height of all Walls
while wallsheight <=0 :
    try:
        wallsheight = float(input("Enter height of walls (m): "))
    except ValueError:
        print("Invalid Value")
#Asking for number of doors and windows
while doorsnum <=0 and wallsheight >= 2.4:
    try:
        doorsnum = int(input("Enter number of doors: "))
    except ValueError:
        print("Invalid Value")
while windowsnum <=0 :
    try:
        windowsnum = int(input("Enter number of windows: "))
    except ValueError:
        print("Invalid Value")
#Windows area and paint calculations
for i in range(windowsnum):
    while windowheight <=0 and windowheight <= wallsheight :
        try:
            windowheight=float(input("Enter window height "+str(i + 1)+": "))
        except ValueError:
            print("Invalid Value")
    while windowwidth<=0 and windowwidth>=wall1width or windowwidth>=wall2width:
        try:
            windowwidth=float(input("Enter window width "+str(i + 1)+": "))
        except ValueError:
            print("Invalid Value")
    windowarea = windowheight * windowwidth
    totalwindowarea = totalwindowarea + windowarea
    windowwidth = -1.0
    windowheight = -1.0
#Area Calculations
doorsarea = doorsnum * (2.4 * 0.4)
wall1area = wall1width * wallsheight
wall2area = wall2width * wallsheight
ceilingarea = wall1width * wall2width
wallsarea = (wall1area + wall2area) * 2
#Calculations for paint required and price of whole room
totalpaint = (wallsarea + ceilingarea - (doorsarea + totalwindowarea))/11
totalprice= totalpaint * 24.68
#Outputting results
print ("Total paint required (L): " + str(totalpaint))
print ("Total price: " + f"${totalprice:.2f}")