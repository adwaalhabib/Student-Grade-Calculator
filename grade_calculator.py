# Student Grade Calculator
# A Beginner Python project for calculating student averages and generating a simple preformance report.

print("=" * 45)
print("STUDENT GRADE CALCULATOR")
print("=" * 45)

# Get the students name
name = input("Enter your name: ")

# Get  the students grades
course1 = float(input("Enter your grade for Mathematics: "))
course2 = float(input("Enter your grade for Physics: "))
course3 = float(input("Enter your grade for Chemistry: "))
course4 = float(input("Enter your grade for Programming: "))

# Calculate the average 
average = (course1 + course2 + course3 + course4) / 4

# Determine the performance level
if average >= 90:
  performance = "Excellent"
elif average >= 80:
  performance = "Very Good"
elif average >= 70:
  performance = "Good"
elif average >= 60:
  performance = "Pass"
else:
  performance = "Needs Improvement"
  
# Display the results
print("\n" + "=" * 45)
print("GRADE REPORT")
print("=" * 45)

print(f"Student: {name}")
print(f"Mathematics: {course1:.1f}")
print(f"Physics: {course2:.1f}")
print(f"Chemistry: {course3:.1f}")
print(f"Programming: {course4:.1f}")

print("-" * 45)
print(f"Average: {average:.2f}")
print(f"Performance: {performance}")

print("=" * 45)
print("Thank you for using the Grade Calculator!")
print("=" * 45)
