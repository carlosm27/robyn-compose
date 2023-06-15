import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

def get_db_connection():
    conn = psycopg2.connect(
        dbname = "robyn_db",
        user = "postgres",
        password = PASSWORD
    )
    return conn

conn = get_db_connection()
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                 'title varchar (150) NOT NULL,'
                                 'author varchar (50) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

cur.execute('INSERT INTO books (title, author)'
            'VALUES (%s, %s)',
            ('A Tale of Two Cities',
             'Charles Dickens')
            )


cur.execute('INSERT INTO books (title, author)'
            'VALUES (%s, %s)',
            ('Anna Karenina',
             'Leo Tolstoy')
            )

conn.commit()

cur.close()
conn.close()