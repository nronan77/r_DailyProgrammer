"""
Challenge:
Given two strings of letters, determine whether the second can be made from the first by removing one letter.
The remaining letters must stay in the same order.

Bonus 1:
Given a string, find all words from the enable1 word list that can be made by removing one letter from the string.
If there are two possible letters you can remove to make the same word, only count it once.
Ordering of the output words doesn't matter.

Bonus 2:
Given an input word from enable1, the largest number of words that can be returned from bonus(word) is 5.
One such input is "boats". There are 28 such inputs in total. Find them all.

Ideally you can do this without comparing every word in the list to every other word in the list.
A good time is around a second. Possibly more or less, depending on your language and platform of choice -
Python will be slower and C will be faster. The point is not to hit any specific run time,
just to be much faster than checking every pair of words.
"""
import sys


def funnel(first_word, second_word):
    if len(first_word) - len(second_word) != 1:
        return False
    else:
        return can_funnel_words(first_word, second_word)


def can_funnel_words(first_word, second_word):
    second_index = 0
    missing_letter_found = False

    for first_index in range(len(first_word)):
        if first_word[first_index].lower() != second_word[second_index].lower():
            if missing_letter_found:
                return False
            else:
                missing_letter_found = True
        elif not missing_letter_found and second_index == len(second_word) - 1:
            return True
        else:
            second_index += 1

    return missing_letter_found


def bonus_one(bonus_word, list_words):
    print(bonus_word)
    results = []

    for list_word in list_words:
        if funnel(bonus_word, list_word):
            results.append(list_word)

    return results


def bonus_two(list_words):
    results = []

    for word in list_words:
        if len(word) <= 3 or len(word) >= 6:
            pass
        elif len(bonus_one(word, list_words)) == 5:
            results.append(word)

    return results


def bonus(bonus_word):
    file = open("../Resources/enable1.txt", "r")
    list_words = file.read().split("\n")
    file.close()

    print("Bonus 1: " + str(bonus_one(bonus_word, list_words)))
    print("Bonus 2: " + str(bonus_two(list_words)))


if __name__ == "__main__":
    if (len(sys.argv) - 1) % 2 == 1:
        bonus_word = sys.argv[len(sys.argv) - 1]
        bonus(bonus_word)
    if len(sys.argv) >= 2:
        first_word = sys.argv[0]
        second_word = sys.argv[1]
    else:
        first_word = input("Please enter the original word: ")
        second_word = input("Please enter the funnel word: ")

    print("Challenge: " + str(funnel(first_word, second_word)))

