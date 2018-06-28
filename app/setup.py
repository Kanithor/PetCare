from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)

sql ="""
CREATE TABLE usuarios 
           (id serial PRIMARY KEY, nombre varchar(40),apellido varchar(40),
           email varchar(100), passwd varchar(255), telefono integer, creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE mascotas
           (id SERIAL PRIMARY KEY, nombre varchar(40), 
           raza varchar, dueno_id integer, creado timestamp);
"""
cur.execute(sql)

sql ="""
CREATE TABLE historial 
           (id PRIMARY KEY, cantidad integer, fecha timestamp);
"""

conn.commit()
cur.close()
conn.close()