# Gradebook System

# Function to determine grade based on score
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Ask number of students
num_students = int(input("Enter number of students: "))

grades = {}

# Input student data
for i in range(num_students):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter score for {name}: "))
    grades[name] = score

# Print gradebook
print("\n--- Gradebook ---")
total = 0
for name, score in grades.items():
    grade = get_grade(score)
    print(f"{name}: {score:.0f} ({grade})")
    total += score

# Calculate and display average
average = total / num_students if num_students > 0 else 0
print(f"Average = {average:.1f}")
