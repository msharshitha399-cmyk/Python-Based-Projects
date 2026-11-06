# Step 1: Take student details
name = input("Enter the student name: ")
student_id = input("Enter the student ID: ")
total_marks = int(input("Enter total marks for each subject: "))

# Step 2: Take marks using list and loop
subjects = ["Math", "Science", "Social Science", "English", "Computer"]
marks = []

for subject in subjects:
    mark = int(input(f"Enter {subject} marks obtained: "))
    marks.append(mark)

# Step 3: Calculate total, percentage
total = sum(marks)
percentage = (total / (total_marks * len(marks))) * 100

# Step 4: Find highest and lowest
highest = max(marks)
lowest = min(marks)
highest_subject = subjects[marks.index(highest)]
lowest_subject = subjects[marks.index(lowest)]

# Step 5: Assign remark based on percentage
if percentage >= 85:
    remark = "Distinction!"
elif percentage >= 35:
    remark = "Pass"
else:
    remark = "Fail"

# Step 6: Display results
print("------ Student Result ------")
print("Student Name    :", name)
print("Student ID      :", student_id)
print("Total Marks     :", total, "/", total_marks * len(marks))
print("Percentage      :", round(percentage, 2), "%")
print("Highest Marks   :", highest, "in", highest_subject)
print("Lowest Marks    :", lowest, "in", lowest_subject)
print("Remark          :", remark)
print("----------------------------")