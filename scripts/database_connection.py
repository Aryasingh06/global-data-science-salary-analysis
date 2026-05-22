import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryasql@2106"
)

print("Connection successful")

cursor = conn.cursor()
# create database
cursor.execute(
    "CREATE DATABASE IF NOT EXISTS salary_project"
)

print("Database created successfully")

# use database
cursor.execute("USE salary_project")
print("using salary_project database")

# table creation
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS salary_data (
        employee_id INT,
        age INT,
        gender VARCHAR(20),
        education VARCHAR(50),
        job_title VARCHAR(100),
        years_experience INT,
        country VARCHAR(50),
        salary_usd FLOAT,
        remote_type VARCHAR(20),
        company_size VARCHAR(20),
        industry VARCHAR(50),
        programming_language VARCHAR(50),
        work_hours_per_week INT,
        satisfaction_score FLOAT
    )
    """
)

print("Table created successfully")

# insert dataset into mysql table
import pandas as pd

df = pd.read_csv(r"C:\Users\arya\Documents\all codes\vs code\project\PROJECTS\Global-data-science-salary-analysis\data\cleaned_salary_dataset.csv")

cols = [
    "employee_id",
    "age",
    "gender",
    "education",
    "job_title",
    "years_experience",
    "country",
    "salary_usd",
    "remote_type",
    "company_size",
    "industry",
    "programming_language",
    "work_hours_per_week",
    "satisfaction_score"
]

df = df[cols]

# INSERT QUERY

insert_query = """
INSERT INTO salary_data (
    employee_id,
    age,
    gender,
    education,
    job_title,
    years_experience,
    country,
    salary_usd,
    remote_type,
    company_size,
    industry,
    programming_language,
    work_hours_per_week,
    satisfaction_score
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


#  INSERT DATA

for row in df.itertuples(index=False, name=None):
    cursor.execute(insert_query, row)


# COMMIT & CLOSE

conn.commit()

print("Data inserted successfully")

cursor.close()
conn.close()