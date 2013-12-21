# -*- coding: utf-8 -*-
import sys,csv
from xml.dom.minidom import Document

def convert(input_file, output_file, header, query_text):
    print 'Reading: ', input_file
    print 'Writing: ', input_file
    print 'Data in: ', header

    doc = Document(  )
    results = doc.createElement("searchresult")
    doc.appendChild(results)
    query = doc.createElement("query")
    query.appendChild( doc.createTextNode(query_text) )
    results.appendChild( query )

    count = 0
    checked_header = False

    with open(input_file, 'Ur') as f:
        reader = csv.DictReader(f)
        for row_dict in reader:
            if not checked_header and header not in row_dict:
                print ("Unable to locate column named %s, check case and "
                         "header row in CSV" % header)
                sys.exit(1)
            checked_header = True

            results.appendChild( create_doc_element( doc, query_text,
                                                    row_dict[header], count ) )
            count = count + 1

    with open(output_file, "wb") as f:
        f.write( doc.toprettyxml(indent="  ", encoding="UTF-8") )

def create_doc_element(doc, title_text, text, id):
    n = doc.createElement('document')
    n.setAttribute("id", str(id))

    title = doc.createElement('title')
    title.appendChild( doc.createTextNode( title_text ) )

    url = doc.createElement('url')
    url.appendChild( doc.createTextNode( "http://localhost/" ) )

    snippet = doc.createElement('snippet')
    snippet.appendChild( doc.createTextNode( text ) )


    n.appendChild( title )
    n.appendChild( url )
    n.appendChild( snippet )
    return n

"""  <document id="0">
    <title>default</title>
    <url>http://www.globe.com.ph/</url>
    <snippet>
      Provides mobile communications (GSM) including
      GenTXT, handyphones, wireline services, an
      broadband Internet services.
    </snippet>
  </document>
  <document id="1">
    <title>Skate Shoes by Globe | Time For Change</title>
    <url>http://www.globeshoes.com/</url>
    <snippet>
      Skaters, surfers, and showboarders
      designing in their own style.
    </snippet>
  </document>

  ...

</searchresult>
"""

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print """
Usage:
    python csv_to_xml.py <input file> <col name> <query text>

  i.e.
    python csv_to_xml.py input.xml IN07 "computer failures"

  You need to specify the input file and the column name, and don't
  forget to trim any junk before the header fields. Also don't forget to
  quote query text if it has spaces"""
        sys.exit(1)

    convert( sys.argv[1], sys.argv[1] + '.xml', sys.argv[2], sys.argv[3])