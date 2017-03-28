import requests

DIFFBOT_API_URL = 'http://api.diffbot.com/v3/article'
DIFFBOT_DEV_TOKEN = '51df05bcf1da5a31b08d6d34ef03519f'


def get_article(article_url):
    print(article_url)
    # set request params for API request
    params = {'token': DIFFBOT_DEV_TOKEN,
              'url': article_url,
              'discussion': 'false'}

    res = requests.get(DIFFBOT_API_URL, params)
    print("print: ", res.json())
    res_obj = res.json()['objects'][0]

    return res_obj['text']

if __name__ == '__main__':
    urls_file = open("FellowshipOfTheRing.txt")
    output_file = open('corpus.txt', 'w')

    corpus = ''

    for line in urls_file:
        print(line)
        url = line.strip()
        article = get_article(url)
        corpus += article

    output_file.write(corpus)
    print('Corpus saved to {}'.format(output_file.name))
