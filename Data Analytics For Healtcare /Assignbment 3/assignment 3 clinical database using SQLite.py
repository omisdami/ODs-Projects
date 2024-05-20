#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing the sqlite3 package
import sqlite3 as sql


# In[ ]:


#creating the clinical database


# In[35]:


connection = sql.connect('Clinical_database.db')


# In[30]:


#Define a connection and cursor to interact with the database


# In[4]:


cursor = connection.cursor()


# In[6]:


#creating the patient table


# In[8]:


cursor.execute('CREATE TABLE patient(patient_id INTEGER PRIMARY KEY,last_name TEXT, first_name TEXT, date_of_birth DATE, address TEXT, city TEXT, province TEXT, postal_code TEXT, sex TEXT) )')


# In[9]:


#create the visit table


# In[12]:


cursor.execute('CREATE TABLE visit (visit_id INTEGER PRIMARY KEY,visit_date TEXT, attending_physician TEXT, primary_diagnosis_icd_code TEXT, primary_diagnosis_name TEXT, secondary_diagnosis_icd_code TEXT, secondary_diagnosis_name TEXT, patient_id INTEGER, FOREIGN KEY(patient_id) REFERENCES patient(patient_id))') 


# In[13]:


#create the medication table


# In[14]:


cursor.execute('''CREATE TABLE medication (
             medication_name TEXT,
             medication_code TEXT,
             medication_dose TEXT,
             medication_frequency TEXT,
             medication_route TEXT,
             prescribing_physician TEXT,
             prescription_date DATE,
             patient_id INTEGER,
             FOREIGN KEY(patient_id) REFERENCES patient(patient_id))''')


# In[15]:


#inserting data into patient table


# In[17]:


patients = [
    (1, 'Dami', 'John', '1980-01-01', '123 Maple Street', 'Springfield', 'IL', '12345', 'M'),
    (2, 'Smith', 'Omis', '1975-05-05', '456 Oak Avenue', 'Centerville', 'CA', '67890', 'F'),
    (3, 'Feyi', 'David', '1990-09-09', '789 Birch Lane', 'Hometown', 'TX', '11223', 'M'),
    (4, 'Issac', 'Emily', '1985-12-12', '101 Pine Road', 'Smallville', 'NY', '44556', 'F'),
    (5, 'Williams', 'Abdul', '1970-07-07', '202 Elm Street', 'Metro City', 'FL', '77889', 'M')
]
cursor.executemany('INSERT INTO patient VALUES (?,?,?,?,?,?,?,?,?)', patients)


# In[18]:


#inserting data into visit table


# In[19]:


visits = [
    (1, '2024-03-01', 'Dr. Tomi', 'J18.9', 'Pneumonia, unspecified', None, None, 1),
    (2, '2024-03-02', 'Dr. Maconi', 'E11.9', 'Type 2 diabetes mellitus without complications', 'I10', 'Essential (primary) hypertension', 2),
    (3, '2024-03-03', 'Dr. Kikun', 'K21.9', 'Gastro-esophageal reflux disease without esophagitis', None, None, 3),
    (4, '2024-03-04', 'Dr. Tope', 'F32.9', 'Major depressive disorder, single episode, unspecified', None, None, 4),
    (5, '2024-03-05', 'Dr. Taiwo', 'I20.9', 'Angina pectoris, unspecified', None, None, 5)
]
cursor.executemany('INSERT INTO visit VALUES (?,?,?,?,?,?,?,?)', visits)


# In[20]:


#inserting data into medication table


# In[21]:


medications = [
    ('Amoxicillin', 'A01', '500mg', 'Every 8 hours', 'Oral', 'Dr. Tomi', '2024-03-01', 1),
    ('Metformin', 'M01', '1000mg', 'Twice a day', 'Oral', 'Dr. Maconi', '2024-03-02', 2),
    ('Omeprazole', 'O01', '20mg', 'Once a day', 'Oral', 'Dr. Kikun', '2024-03-03', 3),
    ('Sertraline', 'S01', '50mg', 'Once a day', 'Oral', 'Dr. Tope', '2024-03-04', 4),
    ('Atenolol', 'A02', '100mg', 'Once a day', 'Oral', 'Dr. Taiwo', '2024-03-05', 5)
]
cursor.executemany('INSERT INTO medication VALUES (?,?,?,?,?,?,?,?)', medications)


# In[22]:


#commit the chnages


# In[25]:


connection.commit()


# In[26]:


# Querying and printing all rows from each table


# In[27]:


tables = ['patient', 'visit', 'medication']
for table in tables:
    print(f"Contents of the {table} table:")
    cursor.execute(f'SELECT * FROM {table}')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    print()  


# In[28]:


#close connection to database


# In[29]:


connection.close()


# #Q1
# 
# INTEGER: This data type is used for whole numbers. It can store a variable amount of data ranging from 1 byte to 8 bytes, depending on the magnitude of the value.
# Example: age INTEGER
# 
# TEXT: This data type is used for storing text strings. SQLite stores text based on the database encoding (UTF-8, UTF-16BE, or UTF-16LE).
# Example: first_name TEXT
# 
# REAL: This data type is used for floating-point numbers. It is an 8-byte floating point value similar to the double data type in many other programming languages.
# Example: weight REAL
# 
# BLOB: This stands for Binary Large Object and is used to store binary data, such as images or files, exactly as it was input.
# Example: profile_picture BLOB
# 
# NUMERIC: This is a flexible data type that can store integers, floating point values, or text representing numbers. The way the data is stored depends on the provided value.
# Dates and times are often stored as TEXT (in ISO8601 strings), REAL (as Julian day numbers), or INTEGER (as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC) but are considered under the NUMERIC class because of SQLite's type affinity behavior.
# Example: created_at TIMESTAMP (stored as TEXT, REAL, or INTEGER but behaves numerically)

# #Q2
# 
# A JOIN operation in SQL is used to combine rows from two or more tables based on a related column between them; this is a fundamental operation in relational databases, allowing for the retrieval of data that is distributed across multiple tables; the JOIN operation is essential for queries that need to pull information from various tables to produce a set of results that merges all relevant data.
# 
# INNER JOIN: This is the most common type of JOIN. It returns rows when there is at least one match in both tables. If there is no match, the rows are not returned.
# 
# LEFT JOIN (or LEFT OUTER JOIN): This returns all rows from the left table, and the matched rows from the right table. The result is NULL from the right side if there is no match.
# RIGHT JOIN (or RIGHT OUTER JOIN): Opposite to the LEFT JOIN, it returns all rows from the right table, and the matched rows from the left table. The result is NULL from the left side if there is no match.
# 
# FULL JOIN (or FULL OUTER JOIN): This returns rows when there is a match in one of the tables. It effectively combines the results of both LEFT JOIN and RIGHT JOIN. The result set will include all records from both tables, and fill in NULLs for missing matches on either side.
# 
# CROSS JOIN: This returns a Cartesian product of the two tables, i.e., it returns rows combining each row from the first table with each row from the second table. This type of JOIN does not necessitate any matching condition (unless specifically added in the WHERE clause).
# 
# SELF JOIN: This is not a different JOIN type but a technique to join a table with itself. It is useful for queries where you need to compare rows within the same table.
# 
# NATURAL JOIN: This type of JOIN automatically performs the JOIN operation based on the columns in the two tables that have the same names and compatible data types. It's important to use this with caution as it relies on the column names being exactly the same.

# #Q3
# 
# The UPDATE statement is used to modify existing records in a database table. It allows you to change the values of one or more columns for a set of rows that match a specified condition. This is crucial for maintaining the accuracy and relevance of the data stored in a database.
# 
# Example:
# 
# UPDATE patient
# 
# SET sex = 'F'
# 
# WHERE patient_id = 1;
# 
# The ALTER TABLE statement is used to add, delete, or modify columns in an existing table. It can also be used to add and drop various constraints on an existing table. This statement is essential for evolving a database schema over time without losing data.
# 
# Example:
# 
# ALTER TABLE patient 
# 
# DROP COLUMN last_name;
# 
# 
# The SELECT-FROM-WHERE clause is a combination of clauses used to query data from one or more tables. The SELECT clause specifies the columns to be returned. The FROM clause specifies from which table to retrieve the data, and the WHERE clause applies a condition to filter the records to be returned. This is the most commonly used operation to read data that matches specific criteria.
# 
# Example:
# 
# SELECT last_name
# 
# FROM patient
# 
# WHERE patient_id = 2;
# 
# 
# 
# 

# #Q4
# 
# SQLite, SQL Server, and MySQL are all popular database management systems (DBMS), but they cater to different use cases and environments due to their distinct characteristics and features.
# 
# SQLite
# 
# Embedded Database: SQLite is a software library that provides a relational database management system. Unlike SQL Server and MySQL, SQLite is embedded into the end program. It runs in-process with the application, eliminating the need for a separate server process.
# Zero Configuration: SQLite does not require a separate server to be set up or configured, making it ideal for development, testing, and deployment in environments where simplicity and minimal setup are priorities.
# 
# File-Based: SQLite databases are stored as a single file on disk. This makes it very easy to transport, copy, and manage database files, but may not be suitable for high-volume transactions typical in larger, multi-user applications.
# Read/Write Performance: While SQLite offers excellent read/write performance for low to medium traffic websites, desktop applications, and for use as an application file format, it might not perform as well under high concurrency as SQL Server or MySQL.
# 
# Use Case: Ideal for embedded systems, mobile applications, small to medium-sized websites, and as an application file format.
# 
# 
# SQL Server
# 
# Enterprise Database Management System: Developed by Microsoft, SQL Server is a comprehensive, enterprise-grade DBMS designed for complex applications with high transaction rates and large databases.
# 
# Server-Based: Requires installation on a server. It offers robust features for data recovery, reporting services, data analysis, and more. It’s intended for use in high-volume transaction processing systems and data warehousing.
# 
# Licensing and Cost: SQL Server's advanced features and enterprise support come at a cost. Licensing fees can be significant, which might not be justifiable for small projects or startups.
# 
# Use Case: Widely used in enterprise environments for business intelligence, data warehousing, and for applications that require high levels of data integrity, security, and performance.
# 
# MySQL
# 
# Open-Source Database Management System: MySQL, owned by Oracle Corporation, is one of the most popular open-source RDBMS. It is widely used for web applications and supports a broad array of platforms.
# 
# Server-Based: Like SQL Server, MySQL operates on a client/server model and requires a server installation. It is highly regarded for its performance, reliability, and ease of use.
# 
# Cost: MySQL is free under the GNU General Public License, with paid versions offering additional features and support. This makes it accessible for businesses of all sizes.
# 
# Use Case: MySQL is a go-to choice for web applications and is used by many large-scale websites and online services. It’s also suitable for small to large businesses that need a reliable, scalable database system without the high cost of enterprise solutions.
# 
# In summary, while SQLite is designed for simplicity, ease of use, and minimal setup, making it ideal for embedded databases and small to medium-sized applications, SQL Server and MySQL are better suited for larger, more complex applications requiring robust database management capabilities and high levels of concurrency.

# In[ ]:




