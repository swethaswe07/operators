'''
You are given a temperature in Celsius. You need to convert it to Fahrenheit.
Input and Output Format
Input Format:
A single integer celsius.
Output Format:
A single line containing the temperature in Fahrenheit.
To convert a temperature from Celsius to Fahrenheit, you use the following formula:
Multiply the temperature in Celsius by 9/5.
Add 32 to the result of step 1.
'''

# Program to convert Celsius to Fahrenheit

# Get input for temperature in Celsius
celsius = int(input("Enter temperature in Celsius:\n"))

# Convert Celsius to Fahrenheit using the formula
fahrenheit = (celsius * 9 / 5) + 32

# Display the temperature in Fahrenheit
print(fahrenheit)


'''

Input 1
0
Output 1
32.0
Input 2
25
Output 2
77.0
Input 3
100
Output 3
212.0

'''
