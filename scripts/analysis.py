import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryasql@2106",
    database="salary_project"
)

cursor = conn.cursor()
print("Connected to database")

#FUNCTION TO RUN QUERY
# -----------------------------
def run_query(query, columns):
    cursor.execute(query)
    data = cursor.fetchall()
    return pd.DataFrame(data, columns=columns)


# Overall Salary Statistics

df_overall = run_query("""
SELECT 
    COUNT(*) AS total_records,
    AVG(salary_usd) AS avg_salary,
    MIN(salary_usd) AS min_salary,
    MAX(salary_usd) AS max_salary
FROM salary_data
""", ["total_records", "avg_salary", "min_salary", "max_salary"])

print("\n📊 Overall Salary Stats:")
print(df_overall)


#  Top 10 Highest Paying Job Roles
df_jobs = run_query("""
SELECT job_title, AVG(salary_usd) AS avg_salary
FROM salary_data
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 10
""", ["job_title", "avg_salary"])

print("\n📊 Top 10 Job Roles:")
print(df_jobs)


# Salary by Country
df_country = run_query("""
SELECT country, AVG(salary_usd) AS avg_salary
FROM salary_data
GROUP BY country
ORDER BY avg_salary DESC
""", ["country", "avg_salary"])

print("\n📊 Salary by Country:")
print(df_country.head(10))


# Experience Impact on Salary
df_exp = run_query("""
SELECT years_experience, AVG(salary_usd) AS avg_salary
FROM salary_data
GROUP BY years_experience
ORDER BY years_experience
""", ["experience", "avg_salary"])

print("\n📊 Experience vs Salary:")
print(df_exp)


#  Remote Work Analysis
df_remote = run_query("""
SELECT remote_type, AVG(salary_usd) AS avg_salary
FROM salary_data
GROUP BY remote_type
""", ["remote_type", "avg_salary"])

print("\n📊 Remote Work Impact:")
print(df_remote)


#  CLOSE CONNECTION

cursor.close()
conn.close()

print("\nAnalysis Completed Successfully")