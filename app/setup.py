<<<<<<< HEAD
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
=======
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
>>>>>>> 2a7ff4b1c703d4905ad846630aeab3621467d0fa
