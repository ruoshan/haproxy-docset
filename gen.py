#!/usr/local/bin/python

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag
import sys

if len(sys.argv) != 2:
    print "gen.py {version}"
    sys.exit(1)
else:
    V = sys.argv[1]

db = sqlite3.connect('./docSet.dsidx')
cur = db.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = './Documents'

def gen_index(filename):
    page = open(os.path.join(docpath,filename)).read()
    soup = BeautifulSoup(page)

    for div in soup.find_all('div', {'class': "keyword"}):
        try:
            a = div.b.find_all("a")[1]
            name = a.string
            path = filename + a.attrs["href"]
            cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Directive', path))
        except:
            continue

gen_index(V + "/configuration.html")
gen_index(V + "/management.html")

db.commit()
db.close()
