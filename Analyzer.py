import pandas as pd

# Load CSV data
df = pd.read_csv("Marks.csv")

# Show the original data
print("📋 Student Marks:\n", df)

# Calculate total marks per student
df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)

# Calculate average marks
df["Average"] = df["Total"] / 3

# Display top scorer
top_scorer = df[df["Total"] == df["Total"].max()]

# Display stats
print("\n📊 Total & Average:\n", df[["Name", "Total", "Average"]])
print("\n🏆 Top Scorer:\n", top_scorer[["Name", "Total"]])

# Class average
class_avg = df["Average"].mean()
print("\n📈 Class Average:", round(class_avg, 2))

# Save output
df.to_csv("student_report.csv", index=False)
print("\n✅ Analysis saved to 'student_report.csv'")
