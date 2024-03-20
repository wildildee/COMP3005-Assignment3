import sys
import psycopg2

def main():
  # Check if an argument was provided
  if(len(sys.argv) <= 1):
    print("Please specify operation after the file ie. [python assignment3.py read]")
    return
  # Check which argument was provided
  match sys.argv[1]:
    case "create":
      print("Enter the first name:")
      first_name = input()
      print("Enter the last name:")
      last_name = input()
      print("Enter the email:")
      email = input()
      print("Enter the enrolement date in format [year-mm-dd]:")
      enrollment_date = input()
      addStudent(first_name, last_name, email, enrollment_date)
    case "read":
      getAllStudents()
    case "update":
      print("Enter the student id you want to change below:")
      student_id = input()
      print("Enter the new email:")
      email = input()
      updateStudentEmail(student_id, email)
    case "delete":
      print("Enter the student id you want to delete below:")
      student_id = input()
      deleteStudent(student_id)
    case _:
      print("Invalid operation supplied: " + sys.argv[1])

# Retrieves and displays all records from the students table.
def getAllStudents():
  # Connect to the database
  conn = psycopg2.connect(
    database="Assignment 3",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432"
  )
  #Get cursor
  cur = conn.cursor()

  # Get all rows from the students table and print them
  print("Getting all records from the student table:")
  cur.execute("SELECT * FROM students;")
  for row in cur.fetchall():
    print(row)

  # Close the cursor and connection
  cur.close()
  conn.close()

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date):
  # Connect to the database
  conn = psycopg2.connect(
    database="Assignment 3",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432"
  )
  #Get cursor
  cur = conn.cursor()

  # Insert the new row into the table
  print("Inserting the new student into the table:")
  print(f"({first_name}, {last_name}, {email}, {enrollment_date})")
  cur.execute(f"INSERT INTO students(first_name, last_name, email, enrollment_date) VALUES('{first_name}', '{last_name}', '{email}', '{enrollment_date}');")
  conn.commit()

  # Print the result
  getAllStudents()

  # Close the cursor and connection
  cur.close()
  conn.close()

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
  # Connect to the database
  conn = psycopg2.connect(
    database="Assignment 3",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432"
  )
  #Get cursor
  cur = conn.cursor()

  # Update the email
  print(f"Updating student {student_id}'s email to {new_email}")
  cur.execute(f"UPDATE students SET email = '{new_email}' WHERE student_id = '{student_id}';")
  conn.commit()

  # Print the result
  getAllStudents()

  # Close the cursor and connection
  cur.close()
  conn.close()

# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id):
  # Connect to the database
  conn = psycopg2.connect(
    database="Assignment 3",
    host="localhost",
    user="postgres",
    password="postgres",
    port="5432"
  )
  #Get cursor
  cur = conn.cursor()

  # Delete the user
  print(f"Deleting student {student_id}")
  cur.execute(f"DELETE from students WHERE student_id = '{student_id}';")
  conn.commit()

  # Print the result
  getAllStudents()

  # Close the cursor and connection
  cur.close()
  conn.close()

# If we run the file execute main
if __name__ == '__main__':
  main()