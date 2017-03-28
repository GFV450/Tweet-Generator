def getSourceText():
    source_file = open("The Russian Advance.txt")
    source_text = source_file.readlines()

    return source_text


def convertToList(source_text):
    # Replaces the following characters for blank spaces
    for punctuation in '.,:;()':
        source_text = source_text.replace(punctuation, "")

    # source_text = source_text.replace(".", "").replace(",", "") \
    #               .replace(":", "").replace(";", "") \
    #               .replace("(", "").replace(")", "")

    # Assigns each word to an index in an array
    source_text = source_text.split()

    return source_text


def convertToHistogram(words_list):
    # Created a dictionary for the histogram
    histogram = {}
    for word in words_list:
        if word in histogram:
            # If the word is in the dictionary, add 1 to its value
            histogram[word] += 1
        else:
            # If the word is not in the dictionary, assign it as a key
            # and add 1 to its value
            # histogram.update({word: 1})
            histogram[word] = 1

    return histogram


if __name__ == "__main__":
    # source_text = getSourceText()
    source_text = 'one fish two fish red fish blue fish'

    words_list = convertToList(source_text)

    histogram = convertToHistogram(words_list)
    print(histogram)
