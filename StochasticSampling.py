import Histogram
import random


def getHistogram():
    words_file = open("The Russian Advance.txt")
    words_list = words_file.read()
    histogram = Histogram.histogram(words_list)

    return histogram


def countWords(histogram):
    # Total number of words in the Histogram
    total_words = 0

    # Iterates through the dictionary values to get the total number of words
    for key, value in histogram.items():
        total_words += value

    return total_words


def getWord(histogram, totalWords, randomWord):
    counter = 0

    # 'for' loop that iterates through the histogram looking for the random word
    for key, value in histogram.items():
        # Adds the value of the current word
        counter += value

        # Conditional to define if the value of the current word
        # corresponds to the random word selected
        if counter >= randomWord:
            word = key
            break

    return word


if __name__ == "__main__":
    histogram = getHistogram()

    total_words = countWords(histogram)

    # Selects a random word in the histogram
    random_word = random.randint(0, total_words-1)

    word = getWord(histogram, total_words, random_word)

    print(word)
