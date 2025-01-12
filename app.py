from flask import Flask, render_template, request, redirect, url_for
import pymysql

# Flask app initialization
app = Flask(__name__)

# Database configuration
DB_HOST = 'localhost'
DB_USER = 'root'  # Replace with your MySQL username
DB_PASSWORD = 'harsh000'  # Replace with your MySQL password
DB_NAME = 'hospital_management'


def get_db_connection():
    """Establish a database connection and return the connection object."""
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    """Add a new patient to the database."""
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        gender = request.form['gender']
        diagnosis = request.form['diagnosis']
        contact_number = request.form['contact_number']

        connection = None  # Initialize connection to avoid UnboundLocalError

        try:
            connection = get_db_connection()  # Establish database connection
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO patients (name, age, gender, diagnosis, contact_number)
                    VALUES (%s, %s, %s, %s, %s)
                """, (name, age, gender, diagnosis, contact_number))
                connection.commit()  # Commit the transaction
        except Exception as e:
            # Log the error and display a user-friendly message
            print(f"Error occurred while adding patient: {e}")
            return "An error occurred while adding the patient. Please try again."
        finally:
            if connection:  # Ensure the connection is closed
                connection.close()

        # Redirect to the view patients page after successful addition
        return redirect(url_for('view_patients'))  # Correctly reference 'view_patients'

    # Render the form for adding a new patient
    return render_template('add_patient.html')



@app.route('/view_patients')
def view_patients():
    """Display a list of all patients."""
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM patients")
            patients = cursor.fetchall()
    finally:
        connection.close()

    return render_template('view_patients.html', patients=patients)




@app.route('/delete_patient/<int:id>')
def delete_patient(id):
    """Delete a patient by ID."""
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM patients WHERE id = %s", (id,))
            connection.commit()
    finally:
        connection.close()

    return redirect(url_for('view_patients'))


@app.route('/update_patient/<int:id>', methods=['GET', 'POST'])
def update_patient(id):
    """Update the details of an existing patient."""
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            if request.method == 'POST':
                name = request.form['name']
                age = request.form['age']
                gender = request.form['gender']
                diagnosis = request.form['diagnosis']
                contact_number = request.form['contact_number']

                cursor.execute("""
                    UPDATE patients
                    SET name = %s, age = %s, gender = %s, diagnosis = %s, contact_number = %s
                    WHERE id = %s
                """, (name, age, gender, diagnosis, contact_number, id))
                connection.commit()
                return redirect(url_for('view_patients'))

            cursor.execute("SELECT * FROM patients WHERE id = %s", (id,))
            patient = cursor.fetchone()
    finally:
        connection.close()

    return render_template('update_patients.html', patient=patient)


if __name__ == '__main__':
    app.run(debug=True)
