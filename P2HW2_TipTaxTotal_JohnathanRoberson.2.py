# Find the total expense of the meal
#provide input function for cost of food
meal_cost = float(input('Enter the cost of the meal: '))
#Provide value of tax
tax = meal_cost * 0.07
#Provide value of tip
tip = (meal_cost + tax) * 0.18
#Provide the total expense of the meal
total_expense = meal_cost + tip + tax
#Display the total expense of the meal
print('The total expense of the meal is $', format(total_expense, ',.2f'))
