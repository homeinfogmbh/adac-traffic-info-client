#! /usr/bin/env python3
"""ADAC traffic news API Client."""

from argparse import ArgumentParser, Namespace
from hashlib import md5
from json import dumps
from typing import Any

from requests import post


__all__ = ['get_traffic_news']


URL = 'https://www.adac.de/bff'
QUERY = '''query TrafficNews($filter: TrafficNewsFilterInput!) {
  trafficNews(filter: $filter) {
    ...TrafficNewsItems
    __typename
  }
}

fragment TrafficNewsItems on TrafficNews {
  size
  items {
    ...TrafficNewsItem
    __typename
  }
  __typename
}

fragment TrafficNewsItem on TrafficNewsItem {
  id
  type
  details
  street
  timeLoss
  streetSign {
    streetNumber
    country
    __typename
  }
  headline {
    __typename
    ...TrafficNewsDirectionHeadline
    ...TrafficNewsNonDirectionHeadline
  }
  __typename
}

fragment TrafficNewsDirectionHeadline on TrafficNewsDirectionHeadline {
  from
  to
  __typename
}

fragment TrafficNewsNonDirectionHeadline on TrafficNewsNonDirectionHeadline {
  text
  __typename
}
'''


def md5hash(string: str) -> str:
    """Hashes the given string and return the hex digest."""

    return md5(string.encode()).hexdigest()


def get_headers(query: dict[str, Any]) -> dict[str, str]:
    """Returns the headers for the request."""

    return {
        'content-type': 'application/json',
        # We need to provide a hash to distinguish queries with different
        # parameters from each other. Otherwise the API will return the result
        # of last query regardless of the sent parameters.
        'x-graphql-query-hash': md5hash(dumps(query))
    }


def news_query(state: str, *, country: str = 'D', street: str = '',
               construction_sites: bool = False, traffic_news: bool = True,
               page_number: int = 1) -> dict[str, str]:
    """Returns a traffic news query."""

    return {
        'operationName': 'TrafficNews',
        'variables': {
            'filter': {
                'country': {
                    'country': country,
                    'federalState': state,
                    'street': street,
                    'showConstructionSites': construction_sites,
                    'showTrafficNews': traffic_news,
                    'pageNumber': page_number
                }
            }
        },
        'query': QUERY
    }


def get_traffic_news(
        state: str, *, country: str = 'D', street: str = '',
        construction_sites: bool = False, traffic_news: bool = True,
        page_number: int = 1) -> dict[str, Any]:
    """Returns a traffic news dict."""

    query = news_query(
        state, country=country, street=street, traffic_news=traffic_news,
        construction_sites=construction_sites, page_number=page_number
    )
    return post(URL, json=query, headers=get_headers(query)).json()


def get_args(*, description: str = __doc__) -> Namespace:
    """Return the parsed command line arguments."""

    parser = ArgumentParser(description=description)
    parser.add_argument('state')
    parser.add_argument('-C', '--country', metavar='country', default='D')
    parser.add_argument('-s', '--street', metavar='street')
    parser.add_argument('-n', '--no-traffic-news', action='store_true')
    parser.add_argument('-c', '--construction-sites', action='store_true')
    parser.add_argument('-p', '--page', type=int, metavar='n', default=1)
    return parser.parse_args()


def main() -> None:
    """Runs the script."""

    args = get_args()
    json = get_traffic_news(
        args.state, country=args.country, street=args.street,
        traffic_news=not args.no_traffic_news, page_number=args.page,
        construction_sites=args.construction_sites
    )
    print(dumps(json, indent=2))


if __name__ == '__main__':
    main()
