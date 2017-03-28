import re
import sys


def scrub_punctuation(corpus):
    #  scrubs punctuation
    corpus = re.sub("[;:_*\?!]+", "", corpus)
    # replaces dashes with spaces
    corpus = re.sub("-", " ", corpus)

    return corpus


def scrub_newline(corpus):
    corpus = re.sub("\n", ' ', corpus)

    return corpus


def scrub_title(corpus):
    # scrub Mr. and Mrs.
    corpus = re.sub("[mM][rR][sS]?.", "", corpus)

    return corpus


def scrub_whitespace(corpus):
    # replaces double spaces with single spaces
    corpus = re.sub("  ", " ", corpus)

    return corpus


def scrub_text(corpus):
    corpus = scrub_punctuation(corpus)
    corpus = scrub_newline(corpus)
    corpus = scrub_title(corpus)
    corpus = scrub_whitespace(corpus)

    return corpus


if __name__ == "__main__":
    if len(sys.argv) > 1:
        text_file = sys.argv[1]
        text = open(text_file)
        corpus = text.read()
        corpus = scrub_text(corpus)

        print(corpus)
    else:
        print('No source text filename given as argument')
