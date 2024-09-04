import psycopg2
import os

def get_db():
    conn = psycopg2.connect(
        host='db',
        port='5432',
        database='empleados',
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
        )
    return conn

def execQuery(query, params=None):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(query, params)  # Usa parámetros para prevenir SQL injection
    if query.strip().upper().startswith("SELECT"):
        results = cursor.fetchall()  
        cursor.close()
        conn.close()
        return results
    conn.commit() 
    cursor.close()
    conn.close()

def fetchUsers():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return users

execQuery('CREATE TABLE IF NOT EXISTS users ('
'id SERIAL PRIMARY KEY,'
'name VARCHAR(50) NOT NULL,'
'email VARCHAR(100) UNIQUE NOT NULL,'
'created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')

# execQuery("INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com');")
