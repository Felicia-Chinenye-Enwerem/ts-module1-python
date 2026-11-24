def calculate_meal_cost():
    meal_cost=float(input("What's the meal cost? "))
    tip_percent=float(input("What's the tip percentage? "))
    tip=meal_cost*tip_percent/100
    print(tip)
calculate_meal_cost()
