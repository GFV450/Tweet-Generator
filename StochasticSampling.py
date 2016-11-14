import Histogram
import random


if __name__ == "__main__":
    words_file = open("The Russian Advance.txt")
    words_list = words_file.read()

    histogram = Histogram.histogram(words_list)

    index = random.randint(0, len(histogram)-1)
    print(histogram.keys()[index])
