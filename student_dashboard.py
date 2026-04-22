import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G"],
    "Marks": [85, 90, 78, 92, 64, 65, 95],
}

df = pd.DataFrame(data)

# Function to assign grades
def assign_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "D"

# this is to add grade column
df["Grade"] = df["Marks"].apply(assign_grade)

# Analysis
avg = df["Marks"].mean()
topper = df.loc[df["Marks"].idxmax()]
above_avg = df[df["Marks"] > avg]

print("\n--- Student Dashboard ---")
print("Average Marks:", avg)
print("Topper:", topper["Name"], topper["Marks"])

print("\nStudents Above Average:")
print(above_avg)

print("\nFull Data:")
print(df)

#for visualization
df["Grade"].value_counts().plot(kind='bar')
plt.title("Grade Distribution")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.show()
