import sqlite3

def fetch_student_subjects(database_path):
    # Connect to SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # SQL query to fetch student names and subjects
    query = """
    SELECT
        s.ID_student,
        s.Jmeno AS StudentName,
        s.Primeni AS StudentSurname,
        GROUP_CONCAT(p.Nazev, ', ') AS EnrolledSubjects
    FROM
        studenti s
    JOIN
        studentipredmet sp ON s.ID_student = sp.ID_student
    JOIN
        predmety p ON sp.predmnetID = p.predmnetID
    GROUP BY
        s.ID_student, s.Jmeno, s.Primeni;
    """

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Close the database connection
    conn.close()

    return rows

def main():
    # Provide the correct path to your LibreOffice Base database file (.odb)
    database_path = '/home/tjoslef/skola/imt projekt/Pasek.odb'
    results = fetch_student_subjects(database_path)

    # Print results
    for row in results:
        print(f"Student ID: {row[0]}, Name: {row[1]} {row[2]}, Subjects: {row[3]}")

if __name__ == "__main__":
    main()
