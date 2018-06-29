from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s password=%s"%(database,user,passwd))
cur = conn.cursor()

sql ="""
insert into usuarios (id, nombre, apellido, email, passwd, telefono, creado) values ('0', 
'yerson', 'quiroz', 'yerson.sarria@mail.udp.cl', 'pepitopagadoble', '91621579', now());
"""
cur.execute(sql)
sql ="""
insert into mascotas (id, nombre, raza, dueno_id, creado) values ('0','Apolo',
'Cuyi', '0', now()) returning id;
"""
cur.execute(sql)
conn.commit()
post_id = cur.fetchone()[0]

print post_id

sql ="""insert INTO usuarios (id, nombre, apellido, email, passwd, telefono, creado)
 values ('1',Manuel','Alba','malba@mmae.cl','1234','42',now() );
"""

cur.execute(sql)

sql ="""insert INTO historial (id, cantidad, tipo, fecha)
 values ('0',50,'alimentacion',now() );
"""

cur.execute(sql)


sql ="""insert INTO historial (id, cantidad, tipo, fecha)
 values ('0',150,'relleno',now() );
"""

cur.execute(sql)


conn.commit()
cur.close()
conn.close()