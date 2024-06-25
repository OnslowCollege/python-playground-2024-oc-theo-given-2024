"""
Main.

Created by: Theo
Date: 24 June 2024
"""
#Setting variables
totalwindowarea = 0.0
#Asking for dimensions and number of doors and windows
wall1width = int(input("Enter width of wall 1 (m): "))
wall2width = int(input("Enter width of wall 2 (m): "))
wall1height = int(input("Enter height of walls (m): "))
doorsnum = int(input("Enter number of doors: "))
windowsnum = int(input("Enter number of windows: "))
#Windows area and paint calculations
for i in range(windowsnum):
    windowheight = float(input("Enter height of window " + str(i + 1) + ": "))
    windowwidth = float(input("Enter width of window " + str(i + 1) + ": "))
    windowarea = windowheight * windowwidth
    totalwindowarea = totalwindowarea + windowarea
#Doors area calculation
doorsarea = doorsnum * (2.4 * 0.4)
#Wall 1 Calculation for area
wall1area = wall1width * wall1height
#Wall 2 Calculation for area
wall2area = wall2width * wall1height
#Ceiling Calculation for area
ceilingarea = wall1width * wall2width
#Calculation for area of all walls
wallsarea = (wall1area + wall2area) * 2
#Calculations for paint required and price of whole room
totalpaint = (wallsarea + ceilingarea - (doorsarea + totalwindowarea))/11
totalprice= totalpaint * 24.68
#Outputting results
print ("Total paint required (L): " + str(totalpaint))
print ("Total price: " + f"{totalprice:.2f}")