import psycopg2
import pandas as pd


try
    conn = psycopg2.connect("host = localhost dbname=postgres user=postgres password=root")
except psycopg2.error as e:

print("hello world")