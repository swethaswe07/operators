'''

Extras are runs scored by a means other than a batsman hitting the ball. A batsman is not given credit for extras other than runs scored off the bat from a no ball, and the extras are tallied separately on the scorecard and count only towards the team’s score. the types of extras are No ball, Wide, Bye, Leg-bye and Penalty. 1 Penalty corresponds to 5 runs.
Find the total runs that the Extras contribute to the team’s score, given the number of No-balls, wides, byes, leg-byes and penalty given off by the bowlers in innings.
Input format:
First line of the input contains an integer that corresponds to the number of No-balls.
Second line of the input contain an integer that corresponds to the numbers of wides.
Third line of the input contains an integer that corresponds to the number of byes.
Fourth line of the input contain an integer that corresponds to the numbers of led-byes.
Fifth line of the input contains an integer that corresponds to the numbers of penalty runs.
Output format:
Output should display an integer that returns the total runs that the extras together contribute to team’s total.


'''


# Program to calculate total runs from extras

# Get input for each type of extra
no_balls = int(input("Number of No-balls:\n"))
wides = int(input("Number of Wides:\n"))
byes = int(input("Number of Byes:\n"))
leg_byes = int(input("Number of Leg-byes:\n"))
penalty_runs = int(input("Number of Penalty runs:\n"))

# Calculate total runs from extras
total_extras = (no_balls * 1) + (wides * 1) + (byes * 1) + (leg_byes * 1) + (penalty_runs * 5)

# Display the total runs contributed by extras
print(total_extras)



'''

output
    
Number of No-balls:
2
Number of Wides:
3
Number of Byes:
7
Number of Leg-byes:
1
Number of Penalty runs:
17
98



'''
