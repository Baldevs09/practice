distance = float(input("Distance To College (km): "))
speed = float(input("Average Speed (km/h): "))

current_hours = int(input("Current Hours (24-hour format): "))
current_minutes = int(input("Current Minutes: "))

time_remaining = float(input("Time Remaining until class (minutes): "))

# Convert time remaining from minutes to hours
time_remaining_hours = time_remaining / 60

# Calculate travel time (in hours)
travel_time_hours = distance / speed

# Calculate arrival time in hours
arrival_time_hours = current_hours + (current_minutes / 60) + travel_time_hours

# Convert arrival time to hours and minutes
arrival_hours = int(arrival_time_hours)
arrival_minutes = int((arrival_time_hours - arrival_hours) * 60)

# Calculate time left before class (in minutes)
time_left = time_remaining - (travel_time_hours * 60)

# Output
print(f"\nYou will arrive at college at {arrival_hours:02d}:{arrival_minutes:02d}.")
print(f"Time left before class: {time_left:.2f} minutes.")
