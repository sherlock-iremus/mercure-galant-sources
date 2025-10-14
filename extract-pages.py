import csv
import glob
from lxml import etree
import re

tei_ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
xml_ns = 'http://www.w3.org/XML/1998/namespace'

rows = []

for f in glob.glob('./tei-articles/*.xml'):
    tree = etree.parse(f)
    root = tree.getroot()
    bibl = root.find('.//tei:bibl', namespaces=tei_ns)
    if bibl:
        x = bibl.xpath("string()")
        x = " ".join(x.splitlines())
        x = " ".join(x.split())
        match = re.search(r".* p\.(.*)", x)
        if match:
            x = match.group(1).strip().replace('.', '')
            print(x)
            rows.append([f.split('/')[-1].replace('.xml', ''), x])

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
