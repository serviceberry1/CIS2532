#
## Name:        Valerie Bixler
## Due Date:    Sunday, May 10, 2020
## Class:       CIS 2532-NET01  
## Pgm Name:    Sect17pt2.py  (for Section 17 point 2 on pages 728-741)
##
## Assignment:  Learn & practice Structured Query Language (SQL)
##              with Python and sqlite database.
##              
## Description: Complete all exercises in Section 17.2 of Intro to Python 
##              for Computer Science and Data Science by Paul Deitel, 
##              Harvey Deitel on pages 728-741.
#
#
#Connecting to the Database in Python pg 730 
import sqlite3
connection = sqlite3.connect('books.db') 

#View the authors Table's contents
import pandas as pd
pd.options.display.max_columns = 10

#Use SQL to get all author names from authors table
print("\n",pd.read_sql('SELECT * FROM authors', connection, 
            index_col = ['id']))

#Use SQL and pandas to view the titles table's contents
print("\n",pd.read_sql('SELECT * FROM titles', connection))

#Get first 5 rows from table using head 
df = pd.read_sql('SELECT * FROM author_ISBN', connection)
print("\n",df.head())

#Practice retrieving specific columns
print('\n Retrieve specific columns first name, last name from authors table:\n')
print(pd.read_sql('SELECT first, last FROM authors', connection))

#SQL with WHERE clause
print("\n", "SQL using WHERE clause which specifies query selection criteria:\n")
print(pd.read_sql("""SELECT title, edition, copyright
                  FROM titles
                  WHERE copyright > '2016'""", connection))
                  
#SQL with LIKE using pattern matching with % clause
print("\n", "SQL using LIKE and % for pattern matching. ")
print(" Will show last names starting with D:\n")
print(pd.read_sql("""SELECT id, first, last
                  FROM authors
                  WHERE last LIKE 'D%'""", connection,
                  index_col=['id']))

#SQL with LIKE using pattern matching with underscore and % clause
print("\n", "SQL using underscore and % for pattern matching.")
print(" Will show first names starting with any letter followed by letter b:\n")
print(pd.read_sql("""SELECT id, first, last
                  FROM authors
                  WHERE first LIKE '_b%'""", connection,
                  index_col=['id']))

#SQL with ORDER BY clause to sort in asc or desc order
print("\n SQL produced using an order by to sort titles in ascending order:\n")
print(pd.read_sql('SELECT title FROM titles ORDER BY title ASC', 
                  connection))

#SQL with ORDER BY clause to sort by multiple columns using commas to separate
print("\n SQL that sorts authors by last name, first name:\n")
print(pd.read_sql("""SELECT id, first, last
                  FROM authors
                  ORDER BY last, first""", 
                  connection, index_col=['id']))

#SQL with ORDER BY clause to sort by multiple columns using commas to separate
print("\n SQL that sorts authors by last name descending, first name ascending:\n")
print(pd.read_sql("""SELECT id, first, last
                  FROM authors
                  ORDER BY last DESC, first ASC""", 
                  connection, index_col=['id']))

#SQL combining WHERE and ORDER BY
print("\n SQL that produces all titles that include 'How to Program':\n")
print(pd.read_sql("""SELECT isbn, title, edition, copyright
                  FROM titles
                  WHERE title LIKE '%How to Program'
                  ORDER BY title""", 
                  connection))

#SQL using INNER JOIN to merge tables
print("\n SQL that produces all titles that include 'How to Program':\n")
print(pd.read_sql("""SELECT first, last, isbn
                  FROM authors
                  INNER JOIN author_ISBN
                      on authors.id = author_ISBN.id
                  ORDER BY last, first""", 
                  connection).head())

#Modifying the database with insert and delete
print("\nInsert person Sue Red into authors table:")
print("(know that this person was just inserted to the table...")

cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                          VALUES ('Sue', 'Red')""")
                         
print("\n Print authors table showing new author Sue Red:\n")
print(pd.read_sql('SELECT id, first, last FROM authors',
                  connection, index_col=['id']))

print("\nUpdate Sue Red's last name to Black")
cursor = cursor.execute("""UPDATE authors SET last = 'Black'
                        WHERE last = 'Red' AND first = 'Sue'""")
                         
print("\n Print authors table showing updated author Sue Black:\n")
print(pd.read_sql('SELECT id, first, last FROM authors',
                  connection, index_col=['id']))

print("\nDelete Sue Black from authors table...")
cursor = cursor.execute('DELETE FROM authors WHERE id=6')
                         
print("\n Print authors table showing author Sue Black has been deleted:\n")
print(pd.read_sql('SELECT id, first, last FROM authors',
                  connection, index_col=['id']))

#Self Checks for Section 17.2
# Select from the titles table all the titles and their edition numbers in 
#  descending order by edtion number. Show only first 3 results.
print("\n Print titles table with edition nums in descending order.")
print("  Show only first 3 rows returned.\n")
print(pd.read_sql("""SELECT title, edition FROM titles
                  ORDER BY edition DESC""", connection).head(3))

# Select from authors table all authors whose first names start w/'A'. 
print("\n Print authors from authors table whose first names start w/'A':\n")
print(pd.read_sql("""SELECT * FROM authors
                  WHERE first LIKE 'A%'""", connection))
                  
# Select from titles table all titles that do NOT end w/'How to Program'. 
print("\n Print all titles that do NOT end w/'How to Program':\n")
print(pd.read_sql("""SELECT * FROM titles
                  WHERE title NOT LIKE '%How to Program'
                  ORDER BY title""", connection))

#Always remember to disconnect the database
connection.close()








