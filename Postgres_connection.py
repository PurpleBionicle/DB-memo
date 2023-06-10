import psycopg2
from psql_credentials import *

if __name__=='__main__':
    # пытаемся подключиться к базе данных
    conn = psycopg2.connect(dbname=Postgres.dbname, user=Postgres.user,
                            password=Postgres.password, host=Postgres.host)
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM material')
        all_users = curs.fetchall()
        print(all_users)
