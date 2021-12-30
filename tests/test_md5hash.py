"""Test md5hash()."""

from unittest import TestCase

from adac import md5hash


class TestMD5Hashes(TestCase):

    def test_BB(self):
        self.assertEqual(md5hash('BB'), '9d3d9048db16a7eee539e93e3618cbe7')

    def test_BE(self):
        self.assertEqual(md5hash('BE'), 'd3dcf429c679f9af82eb9a3b31c4df44')

    def test_BW(self):
        self.assertEqual(md5hash('BW'), '81043f8c681575bca3e4eff6afbd9db9')

    def test_BY(self):
        self.assertEqual(md5hash('BY'), '925ab312a51a924ab68d9812baa788ff')

    def test_HB(self):
        self.assertEqual(md5hash('HB'), '5651d908d5b3ab8d4a8fe8089b4e7d83')

    def test_HE(self):
        self.assertEqual(md5hash('HE'), 'bc781c76baf5589eef4fb7b9247b89a0')

    def test_HH(self):
        self.assertEqual(md5hash('HH'), 'faafc315b95987fc2b071bcd8f698b81')

    def test_MV(self):
        self.assertEqual(md5hash('MV'), '77d96fc8e5c080038b043ead02dadfc3')

    def test_NI(self):
        self.assertEqual(md5hash('NI'), 'fff6fa4fe7ddec3a931ca45d9e626ae7')

    def test_NW(self):
        self.assertEqual(md5hash('NW'), '7f39ac71e81132daad44925b3bdfde5a')

    def test_RP(self):
        self.assertEqual(md5hash('RP'), 'c4cb0a6bcf9b947b0e647a11ebfacefa')

    def test_SH(self):
        self.assertEqual(md5hash('SH'), 'ec5704f0d56945d1e5b8f9a2384a2b4b')

    def test_SL(self):
        self.assertEqual(md5hash('SL'), '74b8d5453b654b3a79e7b8985a2fc71c')

    def test_SN(self):
        self.assertEqual(md5hash('SN'), '92666505ce75444ee14be2ebc2f10a60')

    def test_ST(self):
        self.assertEqual(md5hash('ST'), 'ec8e57d71f07e31203035548b79d03c8')

    def test_TH(self):
        self.assertEqual(md5hash('TH'), '5b79c40fa7c2bd12dd2df53c4a2b6836')
