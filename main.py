"""
Main.

Created by: Theo
Date: 24 June 2024
"""
#Asking for dimensions
wall1width = int(input("Enter width of wall 1 (m): "))
wall2width = int(input("Enter width of wall 2 (m): "))
wall1height = int(input("Enter height of walls (m): "))
doorsnum = int(input("Enter number of doors: "))
windowsnum = int(input("Enter number of windows: "))
#Wall 1 Calculations for paint required and price
wall1area = wall1width * wall1height
wall1paint = wall1area/11 * 2
wall1price = wall1paint * 24.68
#Wall 2 Calculations for paint required and price
wall2area = wall1height * wall2width
wall2paint = wall2area/11 * 2
wall2price = wall2paint * 24.68
#Ceiling Calculations for paint required and price
ceilingarea = wall1width * wall2width
ceilingpaint = ceilingarea/11 * 2
ceilingprice = ceilingpaint * 24.68
#Calculations for paint required and price of all walls
wallspaint = wall1paint + wall2paint * 2
wallsprice = wallspaint * 24.68
#Calculations for paint required and price of whole room
totalpaint = wallspaint + ceilingpaint
totalprice= wallsprice + ceilingprice
#Outputting results
print ("Total paint required (L): " + str(totalpaint))
print ("Total price: " + f"{wallsprice:.2f}")