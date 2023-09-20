import math

num_of_pennies = input("Please enter the number of your pennies: ")
num_of_pennies = float(num_of_pennies)

p_in_dollar = 100
p_in_quarter = 25
p_in_dime = 10
p_in_nickel = 5
p_in_pen = 1

# num_of_dollars = num_of_pennies // p_in_dollar
num_of_dollars = math.floor(num_of_pennies / p_in_dollar)
print("You have", num_of_dollars, "Dollars")
the_change = num_of_pennies % p_in_dollar
num_of_quarter = math.floor(the_change / p_in_quarter)
print("You have", num_of_quarter, "Quarter")
the_change = num_of_pennies % p_in_quarter
num_of_dime = math.floor(the_change / p_in_dime)
print("You have", num_of_dime, "Dime")
the_change = num_of_pennies % p_in_dime
num_of_nickel = math.floor(the_change / p_in_nickel)
print("You have", num_of_nickel, "Nickel")
the_change = num_of_pennies % p_in_nickel
num_of_pen = math.floor(the_change / p_in_pen)
print("You have", num_of_pen, "Pennies")
the_change = num_of_pennies % p_in_pen
