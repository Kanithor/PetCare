from config import *
import psycopg2

conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql="""
    DROP SCHEMA public CASCADE;
    CREATE SCHEMA public;
    CREATE TABLE users
        (id SERIAL PRIMARY KEY, name VARCHAR, mail varchar, cellphone varchar, address varchar);
    CREATE TABLE pets
        (id SERIAL PRIMARY KEY, raza varchar, dueno_id INTEGER);
    """

cur.execute(sql)
conn.commit()
cur.close()
conn.close()
