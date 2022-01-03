#! /usr/bin/env python3
"""ADAC traffic news API Client."""

from __future__ import annotations
from argparse import ArgumentParser, Namespace
from hashlib import md5
from itertools import count
from os import linesep
from typing import Any, Iterator, NamedTuple, Optional

from requests import Request, Session


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


class NewsRequest(NamedTuple):
    """Represents a request for traffic news."""

    country: str = 'D'
    state: str = ''
    street: str = ''
    construction_sites: bool = False
    traffic_news: bool = True

    @classmethod
    def from_args(cls, args: Namespace) -> NewsRequest:
        """Create a new request from parsed arguments."""
        return cls(
            country=args.country,
            state=args.state,
            street=args.street,
            construction_sites=args.construction_sites
        )

    def query(self, page: int = 1) -> dict[str, Any]:
        """Return a JSON-ish dict of the query."""
        return {
            'operationName': 'TrafficNews',
            'variables': {
                'filter': {
                    'country': {
                        'country': self.country,
                        'federalState': self.state,
                        'street': self.street,
                        'showConstructionSites': self.construction_sites,
                        'showTrafficNews': self.traffic_news,
                        'pageNumber': page
                    }
                }
            },
            'query': QUERY
        }


class NewsResponse(NamedTuple):
    """representation of a traffic mews response."""

    id: int
    type: str
    country: Optional[str]
    street: str
    street_number: Optional[str]
    headline: Optional[str]
    details: str

    def __str__(self) -> str:
        return linesep.join(self.lines)

    @classmethod
    def from_json(cls, json: dict[str, Any]) -> 'NewsResponse':
        """Create a response from a JSON-ish dict."""
        street_info = json.get('streetSign') or {}

        return cls(
            id=json['id'],
            type=json['type'],
            details=json['details'],
            street_number=street_info.get('streetNumber'),
            street=json['street'],
            country=street_info.get('country'),
            headline=json['headline'].get('text'),
        )

    @property
    def lines(self) -> Iterator[str]:
        """Yield lines for str representation."""
        yield f'Sorte: {self.type}'

        if self.country:
            yield f'Land: {self.country}'

        if self.street_number:
            yield f'Straße: {self.street_number} {self.street}'
        else:
            yield f'Straße: {self.street}'

        if self.headline:
            yield f'Überschrift: {self.headline}'

        yield f'Einzelheiten: {self.details}'


def get_traffic_news_page(
    session: Session,
    news_request: NewsRequest,
    page: int,
) -> dict[str, Any]:
    """Returns the given page of the requested traffic news."""

    request = Request(
        method='POST', url=URL,
        headers={'Accept': 'application/json'},
        json=news_request.query(page)
    )
    prepared = session.prepare_request(request)
    prepared.headers['x-graphql-query-hash'] = md5(prepared.body).hexdigest()

    with session.send(prepared) as response:
        response.raise_for_status()
        return response.json()['data']['trafficNews']


def get_traffic_news(
        session: Session,
        request: NewsRequest
    ) -> Iterator[NewsResponse]:
    """Query traffic news."""

    items = 0

    for page in count(1):
        json = get_traffic_news_page(session, request, page)

        for news in json['items']:
            items += 1
            yield NewsResponse.from_json(news)

        if items >= json['size']:
            break


def get_args(*, description: str = __doc__) -> Namespace:
    """Return the parsed command line arguments."""

    parser = ArgumentParser(description=description)
    parser.add_argument('state')
    parser.add_argument('-c', '--country', metavar='country', default='D')
    parser.add_argument('-s', '--street', metavar='street')
    parser.add_argument('-o', '--construction-sites', action='store_true')
    return parser.parse_args()


def main() -> None:
    """Runs the script."""

    request = NewsRequest.from_args(get_args())

    with Session() as session:
        for news in get_traffic_news(session, request):
            print(news)


if __name__ == '__main__':
    main()
