import sys
from links_extractor import LinksExtractor


def main():
    if len(sys.argv) == 1:
        return print('Please, provide URL to parse links.')

    url = sys.argv[1]
    print(f'Parsing {url}')
    result = LinksExtractor(url).fetch()
    print(f'External count: {result.external_count}. Internal count: {result.internal_count}')


if __name__ == '__main__':
    main()
