'''
You are given principal amount, rate of interest per annum, and time in years. You need to calculate the simple interest.
Input and Output Format
Input Format:
The first line contains the principal amount (principal).
The second line contains the rate of interest (rate) per annum.
The third line contains the time (time) in years.
Output Format:
A single line containing the simple interest calculated.

'''

# Program to calculate simple interest

# Get input for principal, rate, and time
principal = float(input("Enter the principal amount:\n"))
rate = float(input("Enter the rate of interest per annum:\n"))
time = float(input("Enter the time in years:\n"))

# Calculate simple interest using the formula: SI = (P * R * T) / 100
simple_interest = (principal * rate * time) / 100

# Display the calculated simple interest
print(simple_interest)


'''
output

Enter the principal amount:
1000
Enter the rate of interest per annum:
5
Enter the time in years:
2
100.0

Enter the principal amount:
5000
Enter the rate of interest per annum:
8.5
Enter the time in years:
3
1275.0


'''
