
import pandas as pd

# Load employee dataset
df = pd.read_csv("employee.csv")

# Display employee data
print("\n===== EMPLOYEE DATA =====")
print(df)

# Calculate average salary
average_salary = df["Salary"].mean()
print("\nAverage Salary:", average_salary)

# Count employees department-wise
department_count = df["Department"].value_counts()
print("\n===== DEPARTMENT COUNT =====")
print(department_count)

# Filter employees above salary threshold
threshold = float(input("\nEnter salary threshold: "))

filtered_employees = df[df["Salary"] > threshold]

print("\n===== EMPLOYEES ABOVE SALARY THRESHOLD =====")
print(filtered_employees)

# Export filtered employees to CSV
filtered_employees.to_csv("filtered_employees.csv", index=False)

# Export department count to CSV
department_count.to_csv("department_count.csv")

print("\nResults exported successfully!")
