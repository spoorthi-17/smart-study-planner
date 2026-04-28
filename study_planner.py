print("Welcome to Smart Study Planner")

subjects = []

try:
    n = int(input("How many subjects do you have? "))
except ValueError:
    print("❌ Please enter a valid number")
    exit()

for i in range(n):
    sub = input("Enter subject name: ")
    
    try:
        hr = int(input(f"How many hours for {sub}? "))
        pr = int(input(f"Enter priority for {sub} (1-High, 2-Medium, 3-Low): "))
        
        if pr not in [1, 2, 3]:
            print("❌ Invalid priority! Setting default = 3")
            pr = 3
            
    except ValueError:
        print("❌ Invalid input! Using default values")
        hr = 1
        pr = 3

    subjects.append((pr, sub, hr))

subjects.sort()

time_slots = ["Morning", "Afternoon", "Evening"]

print("\nYour Smart Timetable:\n")

plan_output = ""

for i, (pr, sub, hr) in enumerate(subjects):
    slot = time_slots[i % 3]
    line = f"{slot}: Study {sub} for {hr} hours (Priority {pr})"
    print(line)
    plan_output += line + "\n"

with open("study_plan.txt", "w") as file:
    file.write(plan_output)

print("\n✅ Study plan saved to study_plan.txt")
