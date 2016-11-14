import sys
import random


def readFile(num_words, words_list):
    sentence = ""

    for i in range(num_words):
        # index: Randomized number to access a specific words_list word
        index = random.randint(0, len(words_list)-1)
        sentence += (words_list[index][:-1] + " ")

    # Less optimized way:
    # for index, word in enumerate(data):
    #     if random_num == 0 or random_num < index:
    #         random_num = random.randint(index, len(data)-1)
    #     elif random_num == index:
    #         sentence += (word[:-1] + " ")
    #     elif num_words == 0:
    #         break

    return sentence


if __name__ == "__main__":
    words_file = open("/usr/share/dict/words")
    words_list = words_file.readlines()

    # num_words: Number of words to append to the sentence
    num_words = int(sys.argv[1])

    sentence = readFile(num_words, words_list)
    print(sentence)
