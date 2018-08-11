"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result_message = return_score_message(score)
    print(result_message)


def return_score_message(score):
    """Return the correct score message"""
    if score < 0 or score > 100:
        result_message = "Invalid score"
    elif 90 < score <= 100:
        result_message = "Excellent"
    elif 50 < score:
        result_message = "Passable"
    else:
        result_message = "Bad"
    return result_message


main()
