# Global Data Science Salary Analysis
> END TO END DATA ANALYTICS PROJECT USING PYTHON,SQL,MYSQL,EDA
> STATISTICAL TESTING AND DATA VISUALIZATION ON A CUSTOM SYNTHETIC DATASET.

## Project Overview
This project analyzes What factors drive data science salary globally across countries ,job roles
experience level company sizes and remote work types.
unlike most salary projects that use pre built kaggle datasets, this project uses a custom synthetic 
dataset generated using python faker library designed to stimulate realistic global salary distribution
with controlled variability.

> Key Questions Answered 
- Which countries pay the highest Data Science salaries?
- Do remote workers earn more than on-site employees?
- How does experience level affect salary growth?
- Which job roles command the highest compensation?
- Is the salary difference between company sizes statistically significant?

## Key Insights

- ML Engineers and AI ENGINEERS  receive highest  average salary  82984 USD-80000 USD/year.
- USA and Canada show highest salary trend led  with averages of 86,242 USD and 84,416 USD respectively 
-  Remote employees earn highest average salaries compared to onsite employess, earned **~18% more** on average than on-site    employees 
-  Senior-level roles earned **2.4x more** than entry-level roles 
- Large companies offer higher salaries  paid **35% higher** salaries than small companies 
- Salary difference between remote/on-site was **statistically significant** (p < 0.05) 

## 💡 Business Recommendations

1. **For Job Seekers:** Prioritize remote-first companies — the salary premium is 
   real and statistically proven in this analysis.
2. **For Companies:** To attract ML/AI talent, compensation benchmarks must account 
   for global competition, especially from US-based remote roles.
3. **For Career Planning:** Experience level is the single strongest predictor of 
   salary growth — investing in upskilling yields compounding returns.

---

## 🗂️ Project Structure
- 

The project includes:
- Synthetic dataset generation
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Statistical analysis
- MySQL database integration
- SQL-based analytics
- Data visualization

The goal of this project is to identify salary trends across countries, job roles, education levels, company sizes, and remote work types.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- VS Code
- Jupyter Notebook
- Faker

# project structure

Global-data-science-salary-analysis/
│
├── data/
│   ├── raw_salary_dataset.csv
│   └── cleaned_salary_dataset.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── eda_analysis.ipynb
│
├── scripts/
│   ├── generate_dataset.py
│   ├── database_connection.py
│   ├── analysis.py
│   └── visualization.py
│
├── images/
│   ├── avg_salary_country.png
│   ├── job_vs_salary.png
│   ├── experience_salary.png
│   └── remotework.png
│
├── requirements.txt
├── README.md
└── .gitignore

 
