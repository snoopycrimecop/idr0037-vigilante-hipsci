from omero.gateway import BlitzGateway
import pandas

import sys

if len(sys.argv) < 3:
    print """
This script simply gets the IDs of the plates referenced in the
plates.tsv and prints them to std out, e.g.
Plate:1
Plate:2
...

Usage:
python get_plate_ids.py [Plates TSV file] [Screen ID]

Example:
python get_plate_ids.py idr0037-screenA-plates.tsv 2051
"""
    exit(1)

platesFile = sys.argv[1]
screenId = sys.argv[2]

# OMERO credentials
user = "public"
password = "public"
host = "localhost"

##########

plates = set()
df = pandas.read_csv(platesFile, sep='\t', header=None)
for index, row in df.iterrows():
    plates.add(row[0])

conn = BlitzGateway(user, password, host=host)
conn.connect()

screen = conn.getObject("Screen", screenId)
for pl in screen.listChildren():
    if pl.name in plates:
        print 'Plate:%s' % pl.id
