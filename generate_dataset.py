import csv
import random

random.seed(42)  # same data every run, so your results are reproducible

NUM_STUDENTS = 20
DEPARTMENTS = ["Computer Science", "Accounting", "Economics", "Mass Communication", "Law", "Microbiology"]
LEVELS = [100, 200, 300, 400, 500]

rows = []
for i in range(1, NUM_STUDENTS + 1):
    student_id = f"STU{i:03d}"
    department = random.choice(DEPARTMENTS)
    level = random.choice(LEVELS)
    attendance = random.randint(40, 100)

    # Students who attend more tend to score higher, plus some randomness
    score = 0.5 * attendance + random.uniform(10, 45)
    score = round(min(score, 100), 1)

    rows.append([student_id, department, level, attendance, score])

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Student_ID", "Department", "Level", "Attendance_Percentage", "Average_Exam_Score"])
    writer.writerows(rows)

print(f"Done. {NUM_STUDENTS} students saved to students.csv")
