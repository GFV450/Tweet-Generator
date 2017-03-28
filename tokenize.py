import re


def tokenize(text):
    tokens = split_on_whitespace(text)
    return tokens


def split_on_whitespace(text):
    return re.split('\s+', text)


if __name__ == '__main__':
    tokenize()
