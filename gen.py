#!/usr/local/bin/python

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag

db = sqlite3.connect('./docSet.dsidx')
cur = db.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = './Documents'

page = open(os.path.join(docpath,'configuration.html')).read()
soup = BeautifulSoup(page)

for div in soup.find_all('div', {'class': "keyword"}):
    try:
        a = div.b.find_all("a")[1]
        name = a.string
        path = "configuration.html" + a.attrs["href"]
        cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Directive', path))
    except:
        continue

db.commit()
db.close()
