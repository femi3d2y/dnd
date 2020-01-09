#!/bin/bash

python3 << EOF

from application import db, models
import os
from pymysql import connect

db.drop_all()
db.create_all()

connection = connect(
    host = os.getenv('MY_SQL_HOST'),
    user = os.getenv('MY_SQL_USER'),
    password = os.getenv('MY_SQL_PASS'),
    db = os.getenv('MY_SQL_DB'),
    charset = 'utf8mb4'
)


f = open('../data/effects.txt', 'r')
	
try:
	for line in f.readlines():
		with connection.cursor() as cursor:
			cursor.execute("""INSERT INTO effects (effect) VALUES ("%s")"""
			% (line))
			connection.commit()

finally:
	connection.close()
			
f.close()
exit()
EOF
