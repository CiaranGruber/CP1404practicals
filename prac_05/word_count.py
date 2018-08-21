"""
Counts how many words are in a user-entered string

21/08/18 - Word Count. Created by Ciaran Gruber
"""


def main():
    word_to_count = {}
    max_word_length = 0
    text = input('Text: ').split()
    for word in text:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1
        if max_word_length < len(word):
            max_word_length = len(word)
    print()

    words = [[word, count] for word, count in word_to_count.items()]
    words.sort()
    max_count_length = len(str(max(word_to_count.values())))

    for word, count in words:
        print('{:{}}: {:{}}'.format(word, max_word_length, count, max_count_length))


main()
