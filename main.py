"""
Main.

Created by: Theo
Date: 24 June 2024
"""
#Setting variables
totalwinarea = 0.0
wall1width = -1.0
wall2width = -1.0
wallsheight = -1.0
winwidth = -1.0
winheight = -1.0
doorsnum = -1
winnum = -1
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
while winnum <=0 :
    try:
        winnum = int(input("Enter number of windows: "))
    except ValueError:
        print("Invalid Value")
#Windows area and paint calculations
winheight = wallsheight + 1
for i in range(winnum):
    while winheight <= 0 or winheight > wallsheight:
        try:
            winheight=float(input("Enter window height "+str(i + 1)+": "))
        except ValueError:
            print("Invalid Value")
    while winwidth<=0 or winwidth > (wall1width and wall2width):
        try:
            winwidth=float(input("Enter window width "+str(i + 1)+": "))
        except ValueError:
            print("Invalid Value")
    winarea = winheight * winwidth
    totalwinarea = totalwinarea + winarea
    winwidth = -1.0
    winheight = -1.0
#Area Calculations
doorsarea = doorsnum * (2.4 * 0.4)
wall1area = wall1width * wallsheight
wall2area = wall2width * wallsheight
ceilingarea = wall1width * wall2width
wallsarea = (wall1area + wall2area) * 2
#Calculations for paint required and price of whole room
totalpaint = (wallsarea + ceilingarea - (doorsarea + totalwinarea))/11
totalprice= totalpaint * 24.68
#Outputting results
print ("Total paint required (L): " + str(totalpaint))
print ("Total price: " + f"${totalprice:.2f}")