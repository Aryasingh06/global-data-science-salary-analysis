import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aryasql@2106",
    database="salary_project"
)

cursor = conn.cursor()
print("connected to database")

# Average salary by country
cursor.execute("""
SELECT country, AVG(salary_usd) AS avg_salary
FROM salary_data
GROUP BY country
ORDER BY avg_salary DESC               
""")
df1 = pd.DataFrame(cursor.fetchall(), columns=["country", "avg_salary"])

plt.figure()
plt.bar(df1["country"], df1["avg_salary"])
plt.xticks(rotation=45)
plt.title("Avg Salary by Country")
plt.xlabel("Country")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig(r"C:\Users\arya\Documents\all codes\vs code\project\PROJECTS\Global-data-science-salary-analysis\images\avg_salary_country.png")
plt.show()

# Job Title vs Salary
cursor.execute("""
SELECT job_title, AVG(salary_usd) AS avg_salary
FROM salary_data
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 10
""")

df2 = pd.DataFrame(cursor.fetchall(), columns=["job_title", "avg_salary"])

plt.figure()
plt.bar(df2["job_title"], df2["avg_salary"])
plt.xticks(rotation=45)
plt.title("Top 10 Job Roles by Salary")
plt.xlabel("Job Title")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig(r"C:\Users\arya\Documents\all codes\vs code\project\PROJECTS\Global-data-science-salary-analysis\images\job_vs_salary.png")
plt.show()

#  Experience vs Salary

cursor.execute("""
SELECT years_experience, AVG(salary_usd)
FROM salary_data
GROUP BY years_experience
ORDER BY years_experience
""")

df3 = pd.DataFrame(cursor.fetchall(), columns=["experience", "avg_salary"])

plt.figure()
plt.plot(df3["experience"], df3["avg_salary"], marker="o")
plt.title("Experience vs Salary Trend")
plt.xlabel("Years Experience")
plt.ylabel("Salary")
plt.grid(True)
plt.tight_layout()
plt.savefig(r"C:\Users\arya\Documents\all codes\vs code\project\PROJECTS\Global-data-science-salary-analysis\images\experience_salary.png")
plt.show()


# Remote Work Impact
cursor.execute("""
SELECT remote_type, AVG(salary_usd)
FROM salary_data
GROUP BY remote_type
""")

df4 = pd.DataFrame(cursor.fetchall(), columns=["remote_type", "avg_salary"])

plt.figure()
plt.bar(df4["remote_type"], df4["avg_salary"])
plt.title("Remote Work Impact on Salary")
plt.xlabel("Remote Type")
plt.ylabel("Salary")
plt.tight_layout()
plt.savefig(r"C:\Users\arya\Documents\all codes\vs code\project\PROJECTS\Global-data-science-salary-analysis\images\remotework.png")
plt.show()

cursor.close()
conn.close()

print("Analysis completed successfully")