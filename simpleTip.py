"""
Create a program that helps user calculate a range of tips and a total cost for a meal.
When a user enters a value in dollars and cents, your program will calculate three 
possible tip amounts as described below:
1. For excellent service calculate a tip that is 20% of the cost of the meal.
2. For good service calculate a tip that is 15% of the cost of the meal.
3. For poor service calculate a tip that is 10% of the cost of the meal.

Display 4 lines on the screen:
   • The total cost the user entered (1)
   • Each tip and total cost with that tip on separate lines (3)
 
"""

def tip_calc(cost):
    excellent = cost * .20
    good = cost * .15
    poor = cost * .10
    excellent_total = excellent + cost
    good_total = good + cost
    poor_total = poor + cost
    print("\n=============== Tip Results ===================")
    print("Cost of the meal: ${:04.2f}" .format(cost))
    print("Excellent Service tip: ${:04.2f} total: ${:04.2f}" .format(excellent,excellent_total))
    print("Good Service tip: ${:04.2f} total: ${:04.2f}" .format(good,good_total))
    print("Poor Service tip: ${:04.2f} total: ${:04.2f}" .format(poor,poor_total))
    

cost = float(input("Enter the cost of the meal: $ "))

tip_calc(cost)
