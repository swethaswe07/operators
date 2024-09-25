'''
3)MS Dhoni is a grade A player according to BCCI Central Contracts in 2016. MSD's net worth in 2016 is around 31 million and is said to be the richest Indian cricketer.
Apart from his salary as an Indian cricketer, Dhoni endorses various popular brands and earns a large amount from endorsements. Besides that individual and team bonuses are also given on the basis of individual and team performances. So precisely the sources of income for Dhoni are from - Salary, Bonuses and Awards through Winning and Endorsements.
Write a program that finds Dhoni's percentage of income earned from each of the 3 individual sources.
Input Format:
First line of the input is an integer that specifies Dhoni's income in rupees from Salary.
Second line is an integer that specifies Dhoni's income in rupees from Bonuses and Awards.
Third line is an integer that specifies Dhoni's income in rupees from endorsements.
Output Format:
Output should display 3 floats in a line, separated by a space. The first float corresponds to the percentage of income from Salary, the second float corresponds to the percentage of income from Bonuses and Awards and the third float corresponds to the percentage of income from endorsements.
All float values should be displayed correct to 2 decimal places.


'''

# Input: Dhoni's income from Salary, Bonuses, and Endorsements
salary = int(input("Enter Dhoni's income from Salary (in rupees): "))
bonuses = int(input("Enter Dhoni's income from Bonuses and Awards (in rupees): "))
endorsements = int(input("Enter Dhoni's income from Endorsements (in rupees): "))

# Calculate total income
total_income = salary + bonuses + endorsements

# Calculate percentages
salary_percentage = (salary / total_income) * 100
bonuses_percentage = (bonuses / total_income) * 100
endorsements_percentage = (endorsements / total_income) * 100

# Output: percentages formatted to 2 decimal places
print(f"{salary_percentage:.2f} {bonuses_percentage:.2f} {endorsements_percentage:.2f}")




'''

Enter Dhoni's income from Salary (in rupees): 
20000000
Enter Dhoni's income from Bonuses and Awards (in rupees): 
5000000
Enter Dhoni's income from Endorsements (in rupees): 
6000000
64.52 16.13 19.35


'''
