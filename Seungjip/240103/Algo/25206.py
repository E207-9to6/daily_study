lecture_sum = 0
grade_sum = 0

grade_cal = {
    "A+" : 4.5, "A0" : 4.0, "B+": 3.5, "B0" : 3.0,
    "C+" : 2.5, "C0": 2.0, "D+" : 1.5, "D0" : 1.0, "F" : 0}

for _ in range(20):
    subject, lecture, grade = input().split()
    lecture = float(lecture)
    if grade == "P":
        pass
    else:
        lecture_sum += lecture
        grade_sum += grade_cal[grade]*lecture

print(grade_sum/lecture_sum)