###
#-------------------------------------------------------------------------------
# mario.py
#-------------------------------------------------------------------------------
#
# Author:       Alwin Tareen
# Created:      Feb 12, 2021
# Execution:    python3 mario.py
# Check50:      check50 cs50/problems/2021/x/sentimental/mario/less
# Submit50:     submit50 cs50/problems/2021/x/sentimental/mario/less
#
# This program displays a half-pyramid of specified height.
#
##

height = 0
while height < 1 or height > 8:
    height = int(input("Height: "))

for row in range(1, height+1):
    print(" "*(height-row) + "#"*row)

