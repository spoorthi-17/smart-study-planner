print("Welcome to Smart Study Planner")

subjects = []

n = int(input("How many subjects do you have? "))

for i in range(n):
    sub = input("Enter subject name: ")
    hr = int(input(f"How many hours for {sub}? "))
    pr = int(input(f"Enter priority for {sub} (1-High, 2-Medium, 3-Low): "))
    
    subjects.append((pr, sub, hr))

# Sort by priority
subjects.sort()

time_slots = ["Morning", "Afternoon", "Evening"]

print("\nYour Smart Timetable:\n")

plan_output = ""

for i, (pr, sub, hr) in enumerate(subjects):
    slot = time_slots[i % 3]
    line = f"{slot}: Study {sub} for {hr} hours (Priority {pr})"
    print(line)
    plan_output += line + "\n"

# Save to file
with open("study_plan.txt", "w") as file:
    file.write(plan_output)

print("\n✅ Study plan saved to study_plan.txt")
