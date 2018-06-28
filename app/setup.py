from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE usuarios 
           (id serial PRIMARY KEY,rol integer, nombre varchar(40),apellido varchar(40),
           email varchar(100),passwd varchar(255), creado timestamp);
"""

cur.execute(sql)


sql ="""
CREATE TABLE mascota 
           (id serial PRIMARY KEY, nombre varchar, raza varchar, creado timestamp);
"""

cur.execute(sql)

sql ="""
CREATE TABLE historial 
           (id PRIMARY KEY, cantidad integer, fecha timestamp);
"""

conn.commit()
cur.close()
conn.close()