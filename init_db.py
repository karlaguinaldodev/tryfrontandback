import psycopg2

# Database connection parameters (modify these based on your setup)
host = "localhost"
database = "my_project"
user = "postgres"
password = "admin"

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )
    cursor = conn.cursor()
    print("Connected to PostgreSQL!")

    # Create the user table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "user" (
            id SERIAL PRIMARY KEY,
            firstname VARCHAR(50) NOT NULL,
            lastname VARCHAR(50) NOT NULL,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)
    conn.commit()
    print("Table 'user' created successfully!")

    # Insert 5 records
    user_data = [
        ("John", "Doe", "johndoe", "johndoe@example.com", "password123")
    ]

    for user in user_data:
        cursor.execute("""
            INSERT INTO "user" (firstname, lastname, username, email, password)
            VALUES (%s, %s, %s, %s, %s)
        """, user)

    conn.commit()
    print("Inserted 5 users successfully!")

except Exception as e:
    print("Error:", e)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
    print("Database connection closed.")