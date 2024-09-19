'''

Tamilnadu was battling one if it’s worst floods in a century last December, as several part of the state have been submerged and cut off from essential supplies. It was heartening that the Cricketers came forward to contribute for the cause of floods and it was decided amongst the team that the senior players donate 50% of their salary and junior players to donate 40% against the flood relief measures
Assume there are 6 senior players and 5 junior players. The salary of senior players Rs.X and that of junior players is Rs.Y. Find the total contribution from the cricket team towards the floods.
Input format:
First line of the input is an integer “X” that specifies the salary of the senior players in rupees.
Second line is an integer “Y” that specifies the salary of the junior players in rupees.
Output format:
Output should display a flood that gives the total contribution of money in rupees from the cricket team. The float value should be displayed correct to 2 decimal places.


'''

# Program to calculate total contribution from cricket team towards flood relief

# Get input for salaries of senior and junior players
X = int(input("Enter the salary of senior players in rupees:\n"))
Y = int(input("Enter the salary of junior players in rupees:\n"))

# Constants for number of players
senior_players = 6
junior_players = 5

# Calculate contributions
senior_contribution = (X * 0.50) * senior_players
junior_contribution = (Y * 0.40) * junior_players

# Total contribution
total_contribution = senior_contribution + junior_contribution

# Display total contribution formatted to 2 decimal places
print(f"{total_contribution:.2f}")


'''
output
input and output 1:
45000
40000
215000.00
input and output 2:
78000
60000
354000.00
'''
