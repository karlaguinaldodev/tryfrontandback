from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection parameters (Modify these based on your setup)
host="localhost",
database="my_project",
user="postgres",
password="admin"

# Function to connect to the database
def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="my_project",
        user="postgres",
        password="admin"
    )

# Route to display the form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission (POST only)
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            conn = connect_db()
            cursor = conn.cursor()

            # Insert data into users table
            cursor.execute("""
                INSERT INTO "user" (firstname, lastname, username, email, password)
                VALUES (%s, %s, %s, %s, %s)
            """, (firstname, lastname, username, email, password))

            conn.commit()
            cursor.close()
            conn.close()

            return redirect(url_for('success'))

        except Exception as e:
            return f"Error: {e}"

# Success page after form submission
@app.route('/success')
def success():
    return "User registered successfully! <a href='/'>Go back</a>"

if __name__ == '__main__':
    app.run(debug=True)
