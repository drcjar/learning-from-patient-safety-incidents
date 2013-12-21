#audits csv file for field completion

import brewery
from sys import argv

script, inputfilename = argv

b = brewery.create_builder()
b.csv_source("%s" % inputfilename)
b.audit()

b.pretty_printer()

b.stream.run()

