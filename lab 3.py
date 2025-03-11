def assign_grade(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    elif score < 0 or score > 100:
        print("Invalid Score! Please enter a value between 0 and 100.")
    else:
        print("Grade: F")

assign_grade(79)