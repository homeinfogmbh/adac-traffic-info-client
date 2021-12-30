"""ADAC API."""

from enum import Enum
from hashlib import md5
from json import dumps
from sys import argv

from requests import post


URL = 'https://www.adac.de/bff'

QUERY_TRAFFIC_NEWS = '''query TrafficNews($filter: TrafficNewsFilterInput!) {
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


class State(Enum):
    """German states."""
    
    BW = 'Baden-Württemberg'
    BY = 'Bayern'
    BE = 'Berlin'
    BB = 'Brandenburg'
    HB = 'Bremen'
    HH = 'Hamburg'
    HE = 'Hessen'
    MV = 'Mecklenburg-Vorpommern'
    NI = 'Niedersachsen'
    NW = 'Nordrhein-Westfalen'
    RP = 'Rheinland-Pfalz'
    SL = 'Saarland'
    SN = 'Sachsen'
    ST = 'Sachsen-Anhalt'
    SH = 'Schleswig-Holstein'
    TH = 'Thüringen'


def get_headers(state: State, country: str = 'de'):
    """Returns the headers for the request."""
    
    return {
        'content-type': 'application/json',
        # We need to provide a hash to distinguish queries for different
        # states from each other. Otherwise the API will return the result
        # of last query regardless the sent parameters.
        'x-graphql-query-hash': md5(state.name.encode('ascii')).hexdigest(),
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
        'query': QUERY_TRAFFIC_NEWS
    }


def main() -> None:
    """Runs the script."""
    
    state = State[argv[1].upper()]
    response = post(URL, json=news_query(state), headers=get_headers(state))
    print(dumps(response.json(), indent=2))


if __name__ == '__main__':
    main()
