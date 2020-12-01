#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import sqlite3
import sys


db_conn = sqlite3.connect(":memory:")
db = db_conn.cursor()


def url_to_hash(url):
    db.execute('SELECT * FROM url_map WHERE original_url = "%s"' % url)
    print(db.fetchone())


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 shorten_url.py <url>')
        sys.exit(1)

    db.execute('''CREATE TABLE url_map (original_url, shorten_url)''')
    db.execute('''INSERT INTO url_map (original_url, shorten_url) VALUES ("test123", "test123")''')
    db_conn.commit()

    url_to_hash(sys.argv[1])

    db.close()
