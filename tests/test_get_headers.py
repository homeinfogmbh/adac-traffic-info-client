"""Test the get_headers() function."""

from unittest import TestCase

from adac import QUERY, get_headers


STATES = {
    'BB', 'BE', 'BW', 'BY', 'HB', 'HE', 'HH', 'MV', 'NI', 'NW', 'RP', 'SH',
    'SL', 'SN', 'ST', 'TH'
}


class TestGetHeaders(TestCase):

    def test_get_headers_BB(self):
        self.assertEqual(get_headers('BB'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '4446d0d81abd5703523fbce8d4647d41'
        })

    def test_get_headers_BE(self):
        self.assertEqual(get_headers('BE'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '1f792825964bcc92b180edd3fa62befb'
        })

    def test_get_headers_BW(self):
        self.assertEqual(get_headers('BW'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '4dcbc7682b85c9627f6919d58b696122'
        })

    def test_get_headers_BY(self):
        self.assertEqual(get_headers('BY'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': 'ae8bce97e4e4c52fafa561dd7154453e'
        })

    def test_get_headers_HB(self):
        self.assertEqual(get_headers('HB'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '6f024ddda92eb85d3d444d1d58a648cd'
        })

    def test_get_headers_HE(self):
        self.assertEqual(get_headers('HE'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': 'd39fccdd6f9dfcabaf679367ac89b141'
        })

    def test_get_headers_HH(self):
        self.assertEqual(get_headers('HH'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '6d607fec87bb250f2b79413f1ac59a72'
        })

    def test_get_headers_MV(self):
        self.assertEqual(get_headers('MV'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': 'a019ccfefa228b3de686d614c33a85fe'
        })

    def test_get_headers_NI(self):
        self.assertEqual(get_headers('NI'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '653e3448090a7a40696974f463dba4f8'
        })

    def test_get_headers_NW(self):
        self.assertEqual(get_headers('NW'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': 'f1d0d691228e5ffa1addabeee19e310e'
        })

    def test_get_headers_RP(self):
        self.assertEqual(get_headers('RP'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': 'a91d409a7d0f63eeda4ac6ade8cb3d5f'
        })

    def test_get_headers_SH(self):
        self.assertEqual(get_headers('SH'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '9d25081648337b5d95d10107468259d0'
        })

    def test_get_headers_SL(self):
        self.assertEqual(get_headers('SL'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '5c56b54d45addd66954d21eceb2398c7'
        })

    def test_get_headers_SN(self):
        self.assertEqual(get_headers('SN'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '9a93d969dbd7d0c96e0621ab2d8d61cb'
        })

    def test_get_headers_ST(self):
        self.assertEqual(get_headers('ST'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '6d51a03bc88fe6d74b4be017ea8f319d'
        })

    def test_get_headers_TH(self):
        self.assertEqual(get_headers('TH'), {
            'content-type': 'application/json',
            'x-graphql-query-hash': '057665d436ab1f9f7456fdb7d01171ab'
        })


class TestGetHeadersDistinct(TestCase):

    def test_headers_distinct_BB(self):
        for other in (STATES - {'BB'}):
            self.assertNotEqual(get_headers('BB'), get_headers(other))

    def test_headers_distinct_BE(self):
        for other in (STATES - {'BE'}):
            self.assertNotEqual(get_headers('BE'), get_headers(other))

    def test_headers_distinct_BW(self):
        for other in (STATES - {'BW'}):
            self.assertNotEqual(get_headers('BW'), get_headers(other))

    def test_headers_distinct_BY(self):
        for other in (STATES - {'BY'}):
            self.assertNotEqual(get_headers('BY'), get_headers(other))

    def test_headers_distinct_HB(self):
        for other in (STATES - {'HB'}):
            self.assertNotEqual(get_headers('HB'), get_headers(other))

    def test_headers_distinct_HE(self):
        for other in (STATES - {'HE'}):
            self.assertNotEqual(get_headers('HE'), get_headers(other))

    def test_headers_distinct_HH(self):
        for other in (STATES - {'HH'}):
            self.assertNotEqual(get_headers('HH'), get_headers(other))

    def test_headers_distinct_MV(self):
        for other in (STATES - {'MV'}):
            self.assertNotEqual(get_headers('MV'), get_headers(other))

    def test_headers_distinct_NI(self):
        for other in (STATES - {'NI'}):
            self.assertNotEqual(get_headers('NI'), get_headers(other))

    def test_headers_distinct_NW(self):
        for other in (STATES - {'NW'}):
            self.assertNotEqual(get_headers('NW'), get_headers(other))

    def test_headers_distinct_RP(self):
        for other in (STATES - {'RP'}):
            self.assertNotEqual(get_headers('RP'), get_headers(other))

    def test_headers_distinct_SH(self):
        for other in (STATES - {'SH'}):
            self.assertNotEqual(get_headers('SH'), get_headers(other))

    def test_headers_distinct_SL(self):
        for other in (STATES - {'SL'}):
            self.assertNotEqual(get_headers('SL'), get_headers(other))

    def test_headers_distinct_SN(self):
        for other in (STATES - {'SN'}):
            self.assertNotEqual(get_headers('SN'), get_headers(other))

    def test_headers_distinct_ST(self):
        for other in (STATES - {'ST'}):
            self.assertNotEqual(get_headers('ST'), get_headers(other))

    def test_headers_distinct_TH(self):
        for other in (STATES - {'TH'}):
            self.assertNotEqual(get_headers('TH'), get_headers(other))
