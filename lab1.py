def classify_age(age):
    if age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")   
    elif age < 0:
        print("Invalid age. Age cannot be negative.")
    else:
        print("You are a Senior.")

classify_age(55)