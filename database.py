__author__ = 'rmenon'

import psycopg2


def connect():
    """
    Connects to PostgresSQL and returns all the training data
    :return: rows from SequenceData tablecc
    """
    conn = psycopg2.connect("dbname='dictionary' user='postgres' host='localhost' password='Dornsife123'")
    cur = conn.cursor()
    cur.execute("""SELECT * from public.\"SequenceData3\"""")
    rows = cur.fetchall()
    return rows

