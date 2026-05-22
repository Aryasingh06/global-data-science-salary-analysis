# import libraries
import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

countries = {
    "USA": 1.0,
    "Canada": 0.8,
    "Germany": 0.75,
    "UK": 0.72,
    "Australia": 0.78,
    "India": 0.35,
    "Brazil": 0.40,
    "Poland": 0.50
}

job_roles = {
    "Data Analyst": 1.0,
    "Business Analyst": 1.05,
    "Data Scientist": 1.4,
    "Machine Learning Engineer": 1.6,
    "Data Engineer": 1.5,
    "AI Engineer": 1.8,
    "BI Analyst": 1.1,
    "Analytics Engineer": 1.3
}

education_levels = {
    "Bachelors": 1.0,
    "Masters": 1.15,
    "PhD": 1.3
}

company_sizes = {
    "Small": 1.0,
    "Medium": 1.2,
    "Large": 1.5
}

remote_types = [
    "Remote",
    "Hybrid",
    "Onsite"
]

industries = [
    "Finance",
    "Healthcare",
    "E-commerce",
    "EdTech",
    "Retail",
    "Gaming",
    "Consulting",
    "SaaS"
]

programming_languages = [
    "Python",
    "R",
    "SQL",
    "Scala",
    "Julia"
]

tools = [
    "Python",
    "SQL",
    "Pandas",
    "NumPy",
    "Power BI",
    "Tableau",
    "TensorFlow",
    "PyTorch",
    "Spark",
    "Excel"
]

certifications_list = [
    "Google Data Analytics",
    "AWS Certified",
    "Azure Data Engineer",
    "TensorFlow Developer",
    "None",
    "IBM Data Science",
    "Microsoft Power BI"
]

# create empty dataset
data = []

# GENERATE BASIC EMPLOYEE DETAIL
for i in range(1,2000):
    
    age = random.randint(22, 55)

    gender = random.choice([
        "Male",
        "Female",
        "Other"
    ])

    country = random.choice(list(countries.keys()))
    city = fake.city()

    education = random.choice(list(education_levels.keys()))

    job_title = random.choice(list(job_roles.keys()))

    company_size = random.choice(list(company_sizes.keys()))

    remote_type = random.choice(remote_types)

    industry = random.choice(industries)

    programming_language = random.choice(programming_languages)

    years_experience = random.randint(0, 20)

    tools_used = ", ".join(random.sample(tools, 3))

    certification = random.choice(certifications_list)

    work_hours = random.randint(30, 60)

    satisfaction_score = round(random.uniform(4, 10), 1)

    promotion = random.choice([
        "Yes",
        "No"
    ])
    
    # generate experience level 

    if years_experience <= 2:
        experience_level = "Entry"

    elif years_experience <= 5:
        experience_level = "Mid"

    elif years_experience <= 10:
        experience_level = "Senior"

    else:
        experience_level = "Lead"

    # create base salary
    base_salary = 25000

    # apply  salary multipliers
    salary = (
        base_salary
        * countries[country]
        * job_roles[job_title]
        * education_levels[education]
        * company_sizes[company_size]
    )
    # add experience bonus
    salary += years_experience * random.randint(2000, 5000)    

    # Remote work bonus
    if remote_type == "Remote":
        salary += 5000

    #add salary variation
    salary += random.randint(-3000, 3000)

    # final salary cleanup
    salary = round(salary) 

    # intentional missing value
    if random.random() < 0.02:
        salary = np.nan

    if random.random() < 0.03:
        job_title = "Data Scntist"

    if random.random() < 0.01:
        salary = salary * 8

   # Store employeee record
    data.append({
        "employee_id": i,
        "age": age,
        "gender": gender,
        "country": country,
        "city": city,
        "education": education,
        "experience_level": experience_level,
        "years_experience": years_experience,
        "job_title": job_title,
        "industry": industry,
        "programming_langiage":programming_language,
        "company_size": company_size,
        "remote_type": remote_type,
        "tools_used": tools_used,
        "certification":certification,
        "salary_usd": salary,
        "work_hours_per_week": work_hours,
        "satisfaction_score": satisfaction_score,
        "promotion_last_2_years": promotion
    })  
    
df = pd.DataFrame(data)

# Add duplicate rows intentionally
duplicate_rows = df.sample(20)

df = pd.concat([df, duplicate_rows], ignore_index=True)
print(df.head())

    # Save file as CSV
df.to_csv("data/raw_salary_dataset.csv", index=False)

print("Dataset generated successfully")
    #print(df[['job_title','country','salary_usd']].head())
    
