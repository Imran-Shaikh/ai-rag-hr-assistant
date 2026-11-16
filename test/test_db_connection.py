import psycopg # Use 'import psycopg2' if using the older library

try:
    # Use connection string format
    #conn = psycopg.connect("postgresql://postgres:PostgresImran\\@1982@127.0.0.1:5431/postgres")

    conn = psycopg.connect(
         host="127.0.0.1",
         port=5431,
         user="postgres",
         password="PostgresImran@1982",
         dbname="postgres"
    )
    
    print("Successfully connected to local Docker Postgres!")
    conn.close()

except Exception as e:
    print(f"Connection failed: {e}")