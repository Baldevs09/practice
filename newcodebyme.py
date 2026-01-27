#QUESTION =7
target_weight = float(input("Target Weight Loss (kg): "))
days = int(input("Days To Achieve: "))

# Calories needed to burn
total_calories = target_weight * 7700

# Total distance in kilometers
total_distance = total_calories / 60

# Distance per day
km_per_day = total_distance / days

print(f"You need to walk {km_per_day:.2f} kilometers each day to reach your goal.")
