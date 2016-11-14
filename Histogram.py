def histogram(source_text):
    # Replaces the following characters for blank spaces
    source_text = source_text.replace(".", "").replace(",", "") \
                  .replace(":", "").replace(";", "") \
                  .replace("(", "").replace(")", "")

    source_text = source_text.split()
    # print(source_text)

    histogram = {"and": 0}
    for word in source_text:
        try:
            histogram[word] += 1
        except KeyError:
            histogram.update({word: 1})

    return histogram
    # for key, value in dictionary.items():
    #     print(key, value)


if __name__ == "__main__":
    words_file = open("The Russian Advance.txt")
    words_list = words_file.read()

    histogram = histogram(words_list)

    print("It worked!")
