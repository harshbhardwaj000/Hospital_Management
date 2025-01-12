# Hospital Management System

A simple Hospital Management System built using Python, Flask, and MySQL for managing patient details in a hospital. This web-based application allows users to add patient information and view the list of all patients.

## Features
- Add a new patient with details such as name, age, gender, diagnosis, and contact number.
- View a list of all registered patients.
- Simple and user-friendly interface built using HTML, CSS (Bootstrap), and Flask.

## Prerequisites
Before running the project, make sure you have the following installed:

- Python 3.x
- MySQL (or any other database of your choice)
- Flask (Python web framework)


## Folder Structure
```
hospital-management-system/
├── app.py                # Main Flask application
├── templates/
│   ├── index.html        # Home page
│   ├── add_patient.html  # Add patient form
│   └── view_patients.html # View patients page
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```
# Instructions:

## Installation
1. install both of them before run app.py
```pip install flask```
```pip install pymysql```

## Create database 
2. create this database into your mysql before run any thing.
```
CREATE DATABASE hospital_db;

USE hospital_db;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    diagnosis TEXT,
    contact_number VARCHAR(15)
);
```

3. Replace `your-username` and `your-password` with the actual MySQL username and password in the `app.py` file.

```bash
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='your-username',
        password='your-password',
        database='hospital_db'
    )
```
5. Run app.py:
Once the dependencies are installed and the database is set up, you can start the Flask application.

```
python app.py
```
### The application will be available at http://127.0.0.1:5000/.


#### Open your browser and go to http://127.0.0.1:5000/ to access the application.
You can add patient details through the Add Patient form.
You can view the list of all patients by clicking the View Patients button.

4. If you want to add additional details, you can easily extend the `README.md`.

Feel free to customize this file to suit your needs, and happy coding!

## Contributing
Feel free to fork this repository and make improvements. If you have suggestions or fixes, please create a pull request.

## License
This project is open-source and available under the MIT License.

Acknowledgments
Flask documentation for creating the web app.
MySQL for storing patient data.
Bootstrap for styling the front-end.
markdown
Copy code

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/hospital-management-system.git
