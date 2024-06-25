"""
Main.

Created by: Theo
Date: 24 June 2024
"""
#Setting variables
totalwindowarea = 0.0
validanswer = False
#Asking for dimensions and number of doors and windows
while not validanswer:
    wall1width = input("Enter width of wall 1 (m): ")
    if wall1width <= 0:
        print ("Invalid width.")
    else:
        validanswer = True
validanswer = False
while not validanswer:
    wall2width = input("Enter width of wall 2 (m): ")
    if wall2width != type(float) or type(int):
        print("Invalid width")
    elif wall2width <= 0:
        print ("Invalid width.")
    else:
        validanswer = True
validanswer = False
while not validanswer:
    wall1height = int(input("Enter height of walls (m): "))
    if wall1height <= 0:
        print ("Invalid height.")
    else:
        validanswer = True
validanswer = False
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
wall1area = wall1width * wall1height
wall2area = wall2width * wall1height
ceilingarea = wall1width * wall2width
wallsarea = (wall1area + wall2area) * 2
#Calculations for paint required and price of whole room
totalpaint = (wallsarea + ceilingarea - (doorsarea + totalwindowarea))/11
totalprice= totalpaint * 24.68
#Outputting results
print ("Total paint required (L): " + str(totalpaint))
print ("Total price: " + f"${totalprice:.2f}")