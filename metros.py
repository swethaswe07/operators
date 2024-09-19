'''

It were the days of domination from the traditional metros in the team selections and everytime the team is announced for the Indian Squad, mere disappointment was left with this small town player. Dhoni’ill fate continued even during the team selections for the India A squad to tour to Zimbabwe.3 new players from Mumbai were on the list for the Indian team and it was claimed by the selectors that Dhoni was a bit younger than the 3 selected players.
  Assume the 3 players are Named X,Y and Z. The ages of the players X and Y are the same and the age of the Z is 10 more than other 2 players. Given the total age of the 3 players, find the age of the 3 players.
Input format:
First line of the input is an integer that corresponds to the total age of the 3 players.
Output format:
Output should display the ages of the three players in 3 lines. The age of the eldest player should be displayed in the last line.

'''

# Program to calculate the ages of three players based on their total age

# Get input for the total age of the three players
total_age = int(input("Enter the total age of the three players:\n"))

# Let the age of players X and Y be 'a'
# The age of player Z will then be 'a + 10'
# Total age = a + a + (a + 10) = 3a + 10

# Calculate age of player X and Y
a = (total_age - 10) / 3

# Calculate ages of players
age_x = int(a)
age_y = int(a)
age_z = int(a + 10)

# Display the ages
print(age_x)
print(age_y)
print(age_z)


'''
output

input and output 1:
70
20
20
30
input and output 2:
100
30
30
40
