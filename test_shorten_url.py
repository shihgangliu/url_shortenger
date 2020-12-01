#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import unittest
from shorten_url import url_to_hash


class TestURLShortenger(unittest.TestCase):
    def setUp(self):
        self.db_conn = sqlite3.connect(':memory:')
        self.db = self.db_conn.cursor()
        self.db.execute('CREATE TABLE url_map (original_url, shorten_url)')
        self.db.execute('INSERT INTO url_map VALUES("https://www.example.com?q=test123", "12345")')
        self.db_conn.commit()

    def test_invalid_short_url(self):
        self.assertEqual(url_to_hash(self.db, 'https://www.teaches.com/12346'), 'This short url is invalid.')

    def test_valid_short_url(self):
        self.assertEqual(url_to_hash(self.db, 'https://www.teaches.com/12345'), 'https://www.example.com?q=test123')

    def test_existed_url(self):
        self.assertEqual(url_to_hash(self.db, 'https://www.example.com?q=test123'), 'https://www.teaches.com/12345')

    def test_new_url(self):
        short_url = url_to_hash(self.db, 'https://www.example.com?q=test456')
        self.assertTrue(isinstance(short_url, str))
        self.db.execute('SELECT * FROM url_map')
        self.assertEqual(2, len(self.db.fetchall()))

    def tearDown(self):
        self.db_conn.close()


if __name__ == '__main__':
    unittest.main()
