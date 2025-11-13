#  tracker.py
# Name: Sanchita
# Project: Daily Calorie Tracker
# Course: Programming for Problem Solving Using Python (ETCCPP102)

# -------------------------------
# Daily Calorie Tracker Program
# -------------------------------

print("===================================")
print("   Welcome to Daily Calorie Tracker")
print("===================================")
print("Track your meals, calories, and stay healthy!\n")

#--------------------------------
# Task 2: Input & Data Collection
#--------------------------------
meals = []
calories = []

try:
    n = int(input("How many meals do you want to enter today? "))
    for i in range(n):
        meal = input(f"\nEnter meal {i+1} name: ")
        cal = float(input(f"Enter calories for {meal}: "))
        meals.append(meal)
        calories.append(cal)
except ValueError:
    print("❌ Invalid input. Please enter numbers for calories.")
    exit()

#-----------------------------
# Task 3: Calorie Calculations
#-----------------------------
total = sum(calories)
average = total / len(calories)
limit = float(input("\nEnter your daily calorie limit: "))

#------------------------------------
# Task 4: Exceed Limit Warning System
#------------------------------------
print("\nChecking calorie limit status...")
if total > limit:
    print("⚠️  Warning: You have exceeded your daily calorie limit!")
else:
    print("✅ Great! You are within your daily calorie limit.")

#--------------------------------
# Task 5: Neatly Formatted Output
#--------------------------------
print("\n-------- Calorie Summary --------")
print("Meal Name\tCalories")
print("---------------------------------")
for i in range(len(meals)):
    print(f"{meals[i]:<15}\t{calories[i]:.2f}")
print("---------------------------------")
print(f"Total:\t\t{total:.2f}")
print(f"Average:\t{average:.2f}")

#-----------------------------------------
# Task 6 (Bonus): Save Session Log to File
#-----------------------------------------
save = input("\nDo you want to save this session? (yes/no): ").lower()

if save == "yes":
    from datetime import datetime
    filename = "calorie_log.txt"
    with open(filename, "w") as file:
        file.write("=========== Daily Calorie Tracker ===========\n")
        file.write(f"Session Date & Time: {datetime.now()}\n\n")
        file.write("Meal Name\tCalories\n")
        file.write("---------------------------------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}\t{calories[i]:.2f}\n")
        file.write("---------------------------------\n")
        file.write(f"Total:\t\t{total:.2f}\n")
        file.write(f"Average:\t{average:.2f}\n")
        file.write(f"Limit:\t\t{limit:.2f}\n")
        file.write(f"Status:\t\t{'Exceeded Limit ⚠️' if total > limit else 'Within Limit ✅'}\n")
    print(f"💾 Session saved successfully in '{filename}'!")
else:
    print("Session not saved. Exiting program...")

print("\nThank you for using Daily Calorie Tracker!")

