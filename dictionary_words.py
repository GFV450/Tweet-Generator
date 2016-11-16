import sys
import random


def getSourceText():
    source_file = open("/usr/share/dict/words")
    source_text = source_file.readlines()

    return source_text


def readFile(num_words, words_list):
    sentence = ""

    for i in range(num_words):
        # index: Randomized number to access a specific words_list word
        index = random.randint(0, len(words_list)-1)
        # Word is added to the sentence and newline is erased
        sentence += (words_list[index][:-1] + " ")

    return sentence

    # Less optimized way:
    # for index, word in enumerate(data):
    #     if random_num == 0 or random_num < index:
    #         random_num = random.randint(index, len(data)-1)
    #     elif random_num == index:
    #         sentence += (word[:-1] + " ")
    #     elif num_words == 0:
    #         break


if __name__ == "__main__":
    source_text = getSourceText()

    # num_words: Number of words to append to the sentence defined by the user
    num_words = int(sys.argv[1])

    # Reads the source text and returns a sentence
    sentence = readFile(num_words, source_text)

    print(sentence)
