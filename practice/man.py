import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cursor = conn.cursor()

# Create the Employees table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INT PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        BirthDate TEXT,
        HireDate TEXT,
        Position TEXT,
        Salary REAL
    )
''')

# Insert data into the Employees table
employees = [
    (1, 'John', 'Doe', '1980-01-15', '2010-05-23', 'Software Engineer', 80000.00),
    (2, 'Jane', 'Smith', '1985-07-20', '2012-08-01', 'Data Scientist', 90000.00),
    (3, 'Emily', 'Johnson', '1990-03-12', '2015-09-15', 'Project Manager', 85000.00),
    (4, 'Michael', 'Brown', '1975-11-30', '2008-02-22', 'DevOps Engineer', 95000.00),
    (5, 'Sarah', 'Davis', '1988-06-05', '2013-11-11', 'UX Designer', 75000.00)
]

cursor.executemany('''
    INSERT INTO Employees (EmployeeID, FirstName, LastName, BirthDate, HireDate, Position, Salary)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', employees)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()

print("Table created and data inserted successfully.")
