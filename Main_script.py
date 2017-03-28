import sys
import Scrub_text
import tokenize


if __name__ == '__main__':
    if len(sys.argv) > 1:
        text_file = sys.argv[1]
        text = open(text_file)
        corpus = text.read()
        corpus = Scrub_text.scrub_text(corpus)
        token = tokenize.tokenize(corpus)

        print(token)
    else:
        print('No source text filename given as argument')
