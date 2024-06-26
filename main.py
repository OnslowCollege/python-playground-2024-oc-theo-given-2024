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
#Asking for width of Wall 1
print("All values must be a number greater than zero.")
while wall1width <=0 :
    try:
        wall1width = float(input("Enter width of wall 1 (m): "))
    except ValueError:
        print ("Invalid Value")
    if wall1width <= 0:
        print("Invalid Number")
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
doorsnum = int(input("Enter number of doors: "))
windowsnum = int(input("Enter number of windows: "))
#Windows area and paint calculations
for i in range(windowsnum):
    windowheight = float(input("Enter height of window " + str(i + 1) + ": "))
    windowwidth = float(input("Enter width of window " + str(i + 1) + ": "))
    windowarea = windowheight * windowwidth
    totalwindowarea = totalwindowarea + windowarea
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