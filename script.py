import psycopg2
import time
print("hello world")
print("this is python container")
# time.sleep(10)
conn = psycopg2.connect(database = "taxi_data", 
                        user = "root", 
                        host= 'pg_db',
                        password = "root",
                        port = 5432)

# Open a cursor to perform database operations
cur = conn.cursor()
# Execute a command: create datacamp_courses table
cur.execute("""
            DROP TABLE IF EXISTS datacamp_courses;
            CREATE TABLE  datacamp_courses(
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR (50) UNIQUE NOT NULL,
            course_instructor VARCHAR (100) NOT NULL,
            topic VARCHAR (20) NOT NULL);
            """)
# Make the changes to the database persistent
conn.commit()

print("Table created")
# Close cursor and communication with the database


cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Data Visualization with ggplot2','Hugo Bowne-Anderson','R')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Intermediate Python for Data Science','Mike McCarthy','Python')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Machine Learning with scikit-learn','Vicky Boykis','Python')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('SQL for Data Science','Kathryn Hurchla','SQL')");

cur.execute("INSERT INTO datacamp_courses(course_name, course_instructor, topic) VALUES('Introduction to Natural Language Processing','Maggie Matsui','Python')");

print("values inserted in to table")
conn.commit()
cur.close()
conn.close()