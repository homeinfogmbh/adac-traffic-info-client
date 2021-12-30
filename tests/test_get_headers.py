"""Test the get_headers() function."""

from unittest import TestCase

from adac import QUERY, get_headers


STATES = {
    'BB', 'BE', 'BW', 'BY', 'HB', 'HE', 'HH', 'MV', 'NI', 'NW', 'RP', 'SH',
    'SL', 'SN', 'ST', 'TH'
}


class TestGetHeaders(TestCase):

    def test_queriy_distinct_BB(self):
        for other in (STATES - {'BB'}):
            self.assertNotEqual(get_headers('BB'), get_headers(other))

    def test_queriy_distinct_BE(self):
        for other in (STATES - {'BE'}):
            self.assertNotEqual(get_headers('BE'), get_headers(other))

    def test_queriy_distinct_BW(self):
        for other in (STATES - {'BW'}):
            self.assertNotEqual(get_headers('BW'), get_headers(other))

    def test_queriy_distinct_BY(self):
        for other in (STATES - {'BY'}):
            self.assertNotEqual(get_headers('BY'), get_headers(other))

    def test_queriy_distinct_HB(self):
        for other in (STATES - {'HB'}):
            self.assertNotEqual(get_headers('HB'), get_headers(other))

    def test_queriy_distinct_HE(self):
        for other in (STATES - {'HE'}):
            self.assertNotEqual(get_headers('HE'), get_headers(other))

    def test_queriy_distinct_HH(self):
        for other in (STATES - {'HH'}):
            self.assertNotEqual(get_headers('HH'), get_headers(other))

    def test_queriy_distinct_MV(self):
        for other in (STATES - {'MV'}):
            self.assertNotEqual(get_headers('MV'), get_headers(other))

    def test_queriy_distinct_NI(self):
        for other in (STATES - {'NI'}):
            self.assertNotEqual(get_headers('NI'), get_headers(other))

    def test_queriy_distinct_NW(self):
        for other in (STATES - {'NW'}):
            self.assertNotEqual(get_headers('NW'), get_headers(other))

    def test_queriy_distinct_RP(self):
        for other in (STATES - {'RP'}):
            self.assertNotEqual(get_headers('RP'), get_headers(other))

    def test_queriy_distinct_SH(self):
        for other in (STATES - {'SH'}):
            self.assertNotEqual(get_headers('SH'), get_headers(other))

    def test_queriy_distinct_SL(self):
        for other in (STATES - {'SL'}):
            self.assertNotEqual(get_headers('SL'), get_headers(other))

    def test_queriy_distinct_SN(self):
        for other in (STATES - {'SN'}):
            self.assertNotEqual(get_headers('SN'), get_headers(other))

    def test_queriy_distinct_ST(self):
        for other in (STATES - {'ST'}):
            self.assertNotEqual(get_headers('ST'), get_headers(other))

    def test_queriy_distinct_TH(self):
        for other in (STATES - {'TH'}):
            self.assertNotEqual(get_headers('TH'), get_headers(other))
