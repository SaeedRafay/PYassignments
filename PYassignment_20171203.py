import math
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'a', 'b', 'c', 'd']

print("The first three items in the list are:")
print(players[:3])

print("Three items from the middle of the list are:")
midInd = math.floor(len(players)/2)
print(players[midInd-1:midInd+2])
print(players[3:6])

print("The last three items in the list are:")
print(players[-3:])