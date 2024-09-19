'''
 Distance Between Two Points
Problem Statement
Ajay, Binoy, and Chandru decide to play a game of distance calculation. Each of them will give their house coordinates and they need to calculate the distance between Ajay's house and Chandru's house. Given the coordinates of the 2 endpoints of a line (x1,y1)(x_1, y_1)(x1​,y1​) and (x2,y2)(x_2, y_2)(x2​,y2​), write a Python program to find the distance between the points.
Input Format
Input consists of 4 integers. The first integer corresponds to x1x_1x1​. The second integer corresponds to y1y_1y1​. The third and fourth integers correspond to x2x_2x2​ and y2y_2y2​ respectively.
Output Format
Refer to the Sample Input and Output for exact formatting specifications. [All floating point values are displayed correct to 2 decimal places]

'''
import math

# Program to calculate the distance between two points

# Input the coordinates of the two points
x1 = int(input("Enter x1:\n"))
y1 = int(input("Enter y1:\n"))
x2 = int(input("Enter x2:\n"))
y2 = int(input("Enter y2:\n"))

# Calculate the distance using the distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the result formatted to 2 decimal places
print(f"The distance between Ajay's house and Chandru's house is {distance:.2f}")


'''

output

Enter x1:
3
Enter y1:
4
Enter x2:
6
Enter y2:
8

The distance between Ajay's house and Chandru's house is 5.00
 
'''
