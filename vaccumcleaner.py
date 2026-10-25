# Simple Reflex Vacuum Cleaner Agent

A = "Dirty"
B = "Dirty"
location = "A"

while A == "Dirty" or B == "Dirty":
    print("Location:", location)

    if location == "A":
        if A == "Dirty":
            A = "Clean"
            print("Action: Clean A")
        location = "B"

    else:
        if B == "Dirty":
            B = "Clean"
            print("Action: Clean B")
        location = "A"

print("Both rooms are clean!")
