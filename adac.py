"""ADAC API."""

from functools import cache
from hashlib import md5
from json import dumps
from sys import argv
from typing import Any

from requests import post

from mdb import State


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


@cache
def md5hash(string: str) -> str:
    """Hashes the given string and return the hex digest."""

    return md5(string.encode()).hexdigest()


def get_headers(state: State) -> dict[str, str]:
    """Returns the headers for the request."""

    return {
        'content-type': 'application/json',
        # We need to provide a hash to distinguish queries for different
        # states from each other. Otherwise the API will return the result
        # of last query regardless of the sent parameters.
        'x-graphql-query-hash': md5hash(state.name)
    }


def news_query(state: State, *, country: str = 'D', street: str = '',
               construction_sites: bool = False, traffic_news: bool = True,
               page_number: int = 1) -> dict[str, str]:
    """Returns a traffic news query."""

    return {
        'operationName': 'TrafficNews',
        'variables': {
            'filter': {
                'country': {
                    'country': country,
                    'federalState': state.name,
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
        state: State, *, country: str = 'D', street: str = '',
        construction_sites: bool = False, traffic_news: bool = True,
        page_number: int = 1) -> dict[str, Any]:
    """Returns a traffic news dict."""

    return post(
        URL,
        json=news_query(
            state, country=country, street=street, traffic_news=traffic_news,
            construction_sites=construction_sites, page_number=page_number
        ),
        headers=get_headers(state)
    ).json()


def main() -> None:
    """Runs the script."""

    state = State[argv[1].upper()]
    json = get_traffic_news(state)
    print(dumps(json, indent=2))


if __name__ == '__main__':
    main()
