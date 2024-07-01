"""
Main.

Created by: Theo
Date: 24 June 2024
"""
# Setting variables.
total_win_area = 0.0
wall_1_width = -1.0
wall_2_width = -1.0
walls_height = -1.0
win_width = -1.0
win_height = -1.0
doors_num = -1
win_num = -1
# Asking for width of Wall 1.
print("All values must be a number greater than zero.")
while wall_1_width <=0 :
    try:
        wall_1_width = float(input("Enter width of wall 1 (m): "))
    except ValueError:
        print ("Invalid Value")
# Asking for width of Wall 2.
while wall_2_width <=0 :
    try:
        wall_2_width = float(input("Enter width of wall 2 (m): "))
    except ValueError:
        print("Invalid Value")
# Asking for height of all Walls.
while walls_height <=0 :
    try:
        walls_height = float(input("Enter height of walls (m): "))
    except ValueError:
        print("Invalid Value")
# Asking for number of doors and windows.
while doors_num <=0 and walls_height >= 2.4:
    try:
        doors_num = int(input("Enter number of doors: "))
    except ValueError:
        print("Invalid Value")
while win_num <=0 :
    try:
        win_num = int(input("Enter number of windows: "))
    except ValueError:
        print("Invalid Value")
# Windows area and paint calculations.
win_height = walls_height + 1
for i in range(win_num):
    while win_height <= 0 or win_height > walls_height:
        try:
            win_height=float(input("Enter window height "+str(i + 1)+": "))
        except ValueError:
            print("Invalid Value")
    while win_\width<=0 or win_\width > (wall_1_width and wall_2_width):
        try:
            win_\width=float(input("Enter window width "+str(i + 1)+": "))
        except ValueError:
            print("Invalid Value")
    winarea = win_height * win_\width
    total_win_area = total_win_area + winarea
    win_\width = -1.0
    win_height = -1.0
# Area Calculations.
doorsarea = doors_num * (2.4 * 0.4)
wall1area = wall_1_width * walls_height
wall2area = wall_2_width * walls_height
ceilingarea = wall_1_width * wall_2_width
wallsarea = (wall1area + wall2area) * 2
# Calculations for paint required and price of whole room.
totalpaint = (wallsarea + ceilingarea - (doorsarea + total_win_area)) / 11
totalprice= totalpaint * 24.68
# Outputting results.
print ("Total paint required (L): " + str(totalpaint))
print ("Total price: " + f"${totalprice:.2f}")