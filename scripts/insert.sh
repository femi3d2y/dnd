#!/bin/bash

python3 << EOF

import os
from pymysql import connect

connection = connect(
    host = os.getenv('MY_SQL_HOST'),
    user = os.getenv('MY_SQL_USER'),
    password = os.getenv('MY_SQL_PASS'),
    db = os.getenv('MY_SQL_DB'),
    charset = 'utf8mb4'
)


f = open('./effects.txt', 'r')
	
for line in f.readlines():
	try:
		with connection.cursor() as cursor:
			query = "INSERT INTO effects (effect) values ('line')"		
			cursor.execute(query)
			connection.commit()

	finally:
		connection.close()
			
f.close()
exit()
EOF
