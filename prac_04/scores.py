"""
CP1404/CP5632 Practical
Debugging exercise: almost-working version of a CSV scores file program.
The scores.csv file stores scores for each subject for 10 people.
This code reads the lines into lists, saves the first line as a list of subject codes and
converts the rest of the lines from a list of strings into a list of numbers,
which it then prints with the maximum value for that subject.
Nice. Except, it’s broken! It reads the lists per user not per subject so the results are incorrect.
Use the debugger to follow what it's doing... then fix it.
"""


def main():
    """Read and display student scores from scores file."""
    with open("scores.csv") as scores_file:
        scores_data = scores_file.readlines()
    subjects = scores_data[0].strip().split(",")

    score_values = []
    for score_line in scores_data[1:]:
        score_strings = score_line.strip().split(",")
        score_numbers = [int(value) for value in score_strings]
        if not score_values:
            for x in range(len(score_numbers)):
                score_values.append([score_numbers[x]])
        else:
            index = 0
            for score in score_numbers:
                score_values[index].append(score)
                index += 1

    for i in range(len(subjects)):
        print(subjects[i], "Scores:")
        for score in score_values[i]:
            print(score)
        print('Min:', min(score_values[i]))
        print("Max:", max(score_values[i]))
        print("Average: {:.1f}".format(sum(score_values[i]) / len(score_values[i])))
        print()
        print('Table:')
        for x in range(len(score_values[i])):
            print('______', end='')
        print()
        for score in score_values[i]:
            print('| {:<3} '.format(score), end='')
        print('|')
        for x in range(len(score_values[i])):
            print('------', end='')
        print()
        print()


main()