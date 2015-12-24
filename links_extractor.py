#!/usr/bin/env python3

import requests
import sys
from lxml import etree
from urllib.parse import urljoin

__author__ = 'Cristian Cabrera'
__version__ = '0.0.1'
__license__ = 'MIT'

__all__ = [
    'LinksExtractor',
    'RequestException',
    'ParserException',
]


class RequestException(Exception):
    pass


class ParserException(Exception):
    pass


class LinksExtractor:
    def __init__(self, requests, etree, url):
        self.url = url
        try:
            r = requests.get(url)
        except:
            raise RequestException()
        try:
            self.html = etree.HTML(r.text)
        except:
            raise ParserException()

    def extract(self):
        urls = self.html.xpath('//a/@href')
        urls = [urljoin(self.url, u) for u in urls]
        return urls


def _parse_args():
    """Parse command line arguments."""
    import argparse
    parser = argparse.ArgumentParser(description='Links extractor.')
    arg = parser.add_argument
    arg('url')
    args = parser.parse_args()
    return parser, args


if __name__ == '__main__':
    parser, args = _parse_args()
    try:
        extractor = LinksExtractor(requests, etree, args.url)
    except RequestException:
        print('error: error requesting %s' % args.url)
        sys.exit(1)
    except ParserException:
        print('error: parsing html from %s' % args.url)
        sys.exit(1)
    except Exception:
        print('error: unknown error')
        exit(1)
    links = extractor.extract()
    for link in links:
        print(link)
