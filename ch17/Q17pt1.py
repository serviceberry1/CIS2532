#
## Name:        Valerie Bixler
## Due Date:    Sunday, May 10, 2020
## Class:       CIS 2532-NET01  
## Pgm Name:    Q17pt1.py  (for Question 17 point 1 on page 799)
##
## Assignment:  Learn & practice Structured Query Language (SQL)
##              with Python and sqlite database.
##              
## Description: Complete exercise 17.1 of Intro to Python for Computer
##              Science and Data Science by Paul Deitel, Harvey Deitel 
##              on page 799.
#
#
# Import the sqlite database
import sqlite3
connection = sqlite3.connect('books.db') 

#View the authors Table's contents
import pandas as pd
pd.options.display.max_columns = 10

#SQL that sorts all authors in authors table by last name descending
print("\n17.1 a) SQL that sorts all authors in authors table by last name descending:\n")
print(pd.read_sql("""SELECT last
                  FROM authors
                  ORDER BY last DESC""", 
                  connection))

#SQL that sorts all book titles in titles table in ascending order
print("\n17.1 b) SQL that sorts all book titles in titles table in ascending order:\n")
print(pd.read_sql("""SELECT title
                  FROM titles
                  ORDER BY title ASC""", 
                  connection))


#SQL using INNER JOIN to merge tables
print("\n SQL that produces first 5 rows by author:\n")
print(pd.read_sql("""SELECT first, last, isbn
                  FROM authors
                  INNER JOIN author_ISBN
                      on authors.id = author_ISBN.id
                  ORDER BY last, first""", 
                  connection).head())

#SQL that uses an inner join to select all the books for a specific author.
#  Include the title, copyright year, and ISBN. Order the info alphabetically
#  by title.
print("\n17.1 c) SQL that selects all books for specific author 'Paul Deitel'.")
print("        Results are sorted alphabetically by title:\n")
print(pd.read_sql("""SELECT first, last, author_ISBN.isbn, title
                  FROM authors
                  INNER JOIN author_ISBN
                      on authors.id = author_ISBN.id
                  INNER JOIN titles
                      on titles.isbn = author_ISBN.isbn
                  WHERE last = 'Deitel' and first = 'Paul'
                  ORDER BY title""", 
                  connection))

#SQL that uses an inner join to select all the books for a specific author.
#  Include the title, copyright year, and ISBN. Order the info alphabetically
#  by title.
print("\n17.1 c) SQL that selects all books for specific author 'Wald'.")
print("        Results are sorted alphabetically by title:\n")
print(pd.read_sql("""SELECT first, last, author_ISBN.isbn, title
                  FROM authors
                  INNER JOIN author_ISBN
                      on authors.id = author_ISBN.id
                  INNER JOIN titles
                      on titles.isbn = author_ISBN.isbn
                  WHERE last = 'Wald'
                  ORDER BY title""", 
                  connection))

##SQL to insert a new author into the authors table.
print("\n17.1 d) SQL inserts new author 'Valerie Bixler' into authors table...")
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO authors (first, last)
                          VALUES ('Valerie', 'Bixler')""")
                         
print("        Print of authors table showing new author Valerie Bixler:\n")
print(pd.read_sql('SELECT id, first, last FROM authors',
                  connection, index_col=['id']))

#SQL to insert a new title for an author. Rem that the book must have an 
#  entry in the author _ISBN table and an entry in the titles table. 
##SQL to insert a new author into the authors table.
print("\n17.1 e) SQL inserts Valerie Bixler's book into titles table...")
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO titles (isbn, title, edition, copyright)
                          VALUES ('0131234567', 
                          "Learning Python with COD's Wonderful Educators",
                          1, '2020')""")
                         
print("        Print of titles table showing new book:\n")
print(pd.read_sql('SELECT title, isbn, edition, copyright FROM titles',
                  connection))

print("\n17.1 e) SQL inserts new info into author_ISBN table...")
cursor = connection.cursor()
cursor = cursor.execute("""INSERT INTO author_ISBN (id, isbn)
                          VALUES (6, '0131234567')""")
                         
print("        Print of author_ISBN table:\n")
print(pd.read_sql('SELECT id, isbn FROM author_ISBN',
                  connection))

#SQL that uses an inner join to select all the books for a specific author.
#  Include the title, copyright year, and ISBN. Order the info alphabetically
#  by title.
print("\n17.1 e) User inner join SQL from (c) to print author 'Bixler'.\n")
print(pd.read_sql("""SELECT first, last, author_ISBN.isbn, title
                  FROM authors
                  INNER JOIN author_ISBN
                      on authors.id = author_ISBN.id
                  INNER JOIN titles
                      on titles.isbn = author_ISBN.isbn
                  WHERE last = 'Bixler'
                  ORDER BY title""", 
                  connection))

#Always remember to disconnect the database (Helps to not get locked in Spyder)
connection.close()