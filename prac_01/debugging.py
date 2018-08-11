"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif 90 < score <= 100:
    print("Excellent")
elif 50 < score:
    print("Passable")
else:
    print("Bad")