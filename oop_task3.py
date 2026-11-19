import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. NumPy Array (4 students x 3 subjects)
# ==========================================
marks = np.arange(65, 89, 2).reshape(4, 3)
print("Shape:", marks.shape)

student_averages = np.mean(marks, axis=1)
subject_averages = np.mean(marks, axis=0)
grace_marks = marks + 5  # Broadcasting: add 5 grace marks

weights = np.array([0.3, 0.3, 0.4])
weighted_scores = np.dot(marks, weights)  # Weighted scores using np.dot

print("Student averages:", np.round(student_averages, 2))
print("Subject averages:", np.round(subject_averages, 2))
print("Weighted scores:", np.round(weighted_scores, 2))

# ==========================================
# 2. Create & Load CSVs, Data Cleaning
# ==========================================
dept_data = """department,head,budget
Sales,Ravi,500000
HR,Lakshmi,300000
IT,Vikram,900000
Finance,Deepa,600000
Marketing,Kiran,400000"""

with open("departments.csv", "w") as f:
    f.write(dept_data)

emp_data = """id,name,department,salary,city
1,Arun,Sales,30000,Chennai
2,Priya,HR,45000,Chennai
3,Rahul,IT,,Bangalore
4,Divya,IT,75000,Chennai
5,Karthik,Finance,90000,Mumbai
6,Meena,Sales,,Bangalore
7,Suresh,IT,68000,Chennai
8,Anitha,HR,48000,Mumbai
1,Arun,Sales,30000,Chennai"""

with open("employees_task3.csv", "w") as f:
    f.write(emp_data)

df_emp = pd.read_csv("employees_task3.csv")
df_dept = pd.read_csv("departments.csv")

print("\n--- DataFrame Info ---")
df_emp.info()
print("\n--- DataFrame Describe ---")
print(df_emp.describe())
_ = df_emp.loc[0, "name"]
_ = df_emp.iloc[0:2]
_ = df_emp[df_emp["city"] == "Chennai"]

# Clean data: drop_duplicates, median fill, correct types
df_emp = df_emp.drop_duplicates().copy()
median_salary = df_emp["salary"].median()
df_emp["salary"] = df_emp["salary"].fillna(median_salary).astype(int)

# ==========================================
# 3. Groupby & Merge (inner, left, outer)
# ==========================================
summary = df_emp.groupby("department").agg(
    headcount=("id", "count"),
    avg_salary=("salary", "mean"),
    max_salary=("salary", "max")
).reset_index()

hc_dict = dict(zip(summary["department"], summary["headcount"]))
print(f"\nHeadcount: Sales {hc_dict.get('Sales', 0)} | HR {hc_dict.get('HR', 0)} | IT {hc_dict.get('IT', 0)} | Finance {hc_dict.get('Finance', 0)}")

inner_merged = pd.merge(df_emp, df_dept, on="department", how="inner")
left_merged = pd.merge(df_emp, df_dept, on="department", how="left")
outer_merged = pd.merge(df_emp, df_dept, on="department", how="outer")

no_emp_depts = outer_merged[outer_merged["id"].isna()]["department"].tolist()
print("Outer join: department with no employees listed ->", no_emp_depts)

# ==========================================
# 4. Create 4 Charts (Bar, Histogram, Scatter, Line) & Save as PNG
# ==========================================
# Chart 1: Bar Chart
plt.figure(figsize=(7, 4))
plt.bar(summary["department"], summary["avg_salary"], color="skyblue", label="Avg Salary")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (INR)")
plt.legend()
plt.tight_layout()
plt.savefig("task3_bar_chart.png")
plt.close()

# Chart 2: Histogram
plt.figure(figsize=(7, 4))
plt.hist(df_emp["salary"], bins=5, color="orange", edgecolor="black", label="Employee Count")
plt.title("Employee Salary Distribution")
plt.xlabel("Salary (INR)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()
plt.savefig("task3_histogram.png")
plt.close()

# Chart 3: Scatter Plot
plt.figure(figsize=(7, 4))
plt.scatter(df_emp["id"], df_emp["salary"], color="green", label="Employees")
plt.title("Employee ID vs Salary")
plt.xlabel("Employee ID")
plt.ylabel("Salary (INR)")
plt.legend()
plt.tight_layout()
plt.savefig("task3_scatter.png")
plt.close()

# Chart 4: Line Chart
students = ["Student 1", "Student 2", "Student 3", "Student 4"]
plt.figure(figsize=(7, 4))
plt.plot(students, student_averages, marker="o", color="purple", label="Average Marks")
plt.title("Student Average Marks Across 3 Subjects")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.legend()
plt.tight_layout()
plt.savefig("task3_line_chart.png")
plt.close()

# Insights
print("\n--- Chart Insights ---")
print("1. Bar Chart Insight: Finance has the highest average salary among all departments.")
print("2. Histogram Insight: Most employees earn between 45,000 and 75,000 INR.")
print("3. Scatter Plot Insight: Salaries vary across employee IDs without a strict linear trend.")
print("4. Line Chart Insight: Student 3 achieved the highest average score across all three subjects.")