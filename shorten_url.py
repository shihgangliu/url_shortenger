#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import sqlite3
import sys


HOST = 'https://www.teaches.com/'


def url_to_hash(db, url):
    if url.startswith(HOST):
        short_url = url.split(HOST)
        db.execute('SELECT original_url FROM url_map WHERE shorten_url = "%s"' % short_url[1])
        original_data = db.fetchone()
        if original_data is None:
            return 'This short url is invalid.'
            sys.exit(1)

        return original_data[0]

    db.execute('SELECT shorten_url FROM url_map WHERE original_url = "%s"' % url)
    existed_data = db.fetchone()
    if existed_data is not None:
        return HOST + existed_data[0]

    while True:
        hash_val = hashlib.sha256(url.encode()).hexdigest()
        db.execute('SELECT shorten_url FROM url_map WHERE shorten_url = "%s"' % hash_val[:5])
        collision_data = db.fetchone()
        if collision_data is None:
            break;

    db.execute('INSERT INTO url_map VALUES ("%s", "%s")' % (url, hash_val[:5]))
    return HOST + hash_val[:5]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 shorten_url.py <url>')
        sys.exit(1)

    db_conn = sqlite3.connect(":memory:")
    db = db_conn.cursor()

    db.execute('CREATE TABLE url_map (original_url, shorten_url)')
    db_conn.commit()

    mapping_url = url_to_hash(db, sys.argv[1])
    print(mapping_url)

    db.close()
    sys.exit(0)
