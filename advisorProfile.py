import pandas as pd
import matplotlib.pyplot as plt

# 1. Clean the data by removing empty rows that do not contain any student ID
df = pd.read_csv("/content/joseCases.csv", on_bad_lines='skip')
df = df.dropna(subset=["Student ID"])

# 2. Count how many students Julio has by counting the student IDs
total_students = len(df)
print(f"Jose has {total_students} students.")

# Update the column names by replacing line breaks with spaces
df.columns = df.columns.str.replace('\n', ' ')

# 3. Determine academic standing based on CUM GPA and create a pie chart
def academic_standing(gpa):
    if gpa == 0:
        return "GPA Not Updated"
    elif gpa < 2.0:
        return "Academic Notice"
    else:
        return "Good Academic Standing"

df["Academic Standing"] = df["CUM GPA"].apply(academic_standing)
academic_standing_counts = df["Academic Standing"].value_counts()

# Print the count of each academic status
print("Academic Status Counts:")
for status, count in academic_standing_counts.items():
    print(f"{status}: {count}")

plt.figure(figsize=(6, 6))
plt.pie(academic_standing_counts, labels=academic_standing_counts.index, autopct="%1.1f%%")
plt.title("Academic Standing Distribution")
plt.show()

# 4. Curate the "Advised?" column and create a pie chart
advised_counts = df["Advised?"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(advised_counts, labels=advised_counts.index, autopct="%1.1f%%")
plt.title("Advised Status Distribution")
plt.show()
print(f"Advised students: {advised_counts['Advised']}")
print(f"Not advised students: {advised_counts['Not Advised']}")

# 5. Analyze the "Registered For Fall 2024?" column and create a pie chart
registered_counts = df["Registered For Fall 2024?"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(registered_counts, labels=registered_counts.index, autopct="%1.1f%%")
plt.title("Registration Status for Fall 2024")
plt.show()
print(f"Registered students: {registered_counts['Registered']}")
print(f"Not registered students: {registered_counts['Not Registered']}")

# 6. Create a bar chart for Advised and Registered status
df["Advised_Registered"] = df["Advised?"] + " and " + df["Registered For Fall 2024?"]
advised_registered_counts = df["Advised_Registered"].value_counts()

plt.figure(figsize=(8, 6))
plt.barh(advised_registered_counts.index, advised_registered_counts)
plt.xlabel("Count of Students")
plt.ylabel("Advised and Registered Status")
plt.title("Registered and Advised")
plt.tight_layout()
plt.show()

print("Advised and Registered Counts:")
for status, count in advised_registered_counts.items():
    print(f"{status}: {count}")