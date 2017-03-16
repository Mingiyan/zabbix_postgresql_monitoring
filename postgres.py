#!/usr/bin/python


import os, sys, time

hostname = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
database = sys.argv[4]


def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute(sys.argv[5])
    mystr = cur.fetchall().__str__()

    mystr2 = ''.join(c for c in mystr if c in '.0123456789')
    print mystr2

import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
doQuery( myConnection )
myConnection.close()

