import psycopg2

from django.db import connection
from django.utils.encoding import force_str


def adapt(text):
    a = psycopg2.extensions.adapt(force_str(text))
    a.prepare(connection.connection)
    return a
