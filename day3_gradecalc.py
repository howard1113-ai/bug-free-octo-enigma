def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

n = int(input("Enter number of subjects: "))

scores = []
for i in range(n):
    score = float(input(f"Enter score {i+1}: "))
    scores.append(score)

# Calculate average
average = sum(scores) / n

# Get grade
grade = get_grade(average)

# Print results
print("Scores:", scores)
print("Average:", round(average, 2))
print("Grade:", grade)
