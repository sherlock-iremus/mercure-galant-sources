import glob
from lxml import etree

tei_ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
xml_ns = 'http://www.w3.org/XML/1998/namespace'

NSMAP = {None: 'http://www.tei-c.org/ns/1.0', 'xml': 'http://www.w3.org/XML/1998/namespace'}


def process_livraison_file(f):
    try:
        tree = etree.parse(f)
        root = tree.getroot()
        articles = root.findall('.//tei:div[@type=\'article\']', namespaces=tei_ns)
        for article in articles:
            article_id = article.attrib['{http://www.w3.org/XML/1998/namespace}id']
            if article_id.startswith('MG-'):
                article_id = article_id[3:]
            article_id = article_id.lower()
            article.attrib.pop(f'{{{xml_ns}}}id', None)
            article.attrib.pop('type', None)
            article.attrib.pop('resp', None)

            # New
            new_root = etree.Element('TEI', nsmap=root.nsmap)

            # Create <teiHeader>
            teiHeader = etree.SubElement(new_root, 'teiHeader')
            fileDesc = etree.SubElement(teiHeader, 'fileDesc')

            titleStmt = etree.SubElement(fileDesc, 'titleStmt')
            title = etree.SubElement(titleStmt, 'title')
            title.text = ''

            publicationStmt = etree.SubElement(fileDesc, 'publicationStmt')
            publisher = etree.SubElement(publicationStmt, 'publisher')
            publisher.text = ''

            sourceDesc = etree.SubElement(fileDesc, 'sourceDesc')
            p_source = etree.SubElement(sourceDesc, 'p')

            text = etree.SubElement(new_root, 'text')
            body = etree.SubElement(text, 'body')
            body.append(article)

            new_tree = etree.ElementTree(new_root)
            fout = f"./tei-articles/{article_id}.xml"
            new_tree.write(fout, encoding='utf-8', pretty_print=True, xml_declaration=True)
            print(f"💾 ./tei-articles/{article_id}.xml")
    except Exception as e:
        print(f'🚨 fichier pourri : {f}')
        print(e)


for f in glob.glob('./tei-edition/*.xml'):
    print(f)
    process_livraison_file(f)
