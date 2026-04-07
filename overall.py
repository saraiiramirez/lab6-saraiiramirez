def student_averages(students):
    averages = {}


    for student_id, grades in students.items():
        total_score = sum(grades.values())
        num_assignments = len(grades)
        avg = round(total_score / num_assignments)
        averages[student_id] = avg

    return averages

def assignment_averages(students):
    hw_scores = {}
    for grades in students.values():
        for assignment, score in grades.items():
            if assignment not in hw_scores:
                hw_scores[assignment] = []
            hw_scores[assignment].append(score)

    averages = {}

    for assignment, scores in hw_scores.items():
        total_score = sum(scores)
        num_students = len(scores)
        avg = round(total_score / num_students)
        averages[assignment] = avg

    return averages

students = {
  "s1": {"hw1": 80, "hw2": 90, "hw3": 100},
  "s2": {"hw1": 70, "hw2": 75, "hw3": 85},
  "s3": {"hw1": 95, "hw2": 85, "hw3": 90}
}

print(student_averages(students))
# Esperado:
# {'s1': 90, 's2': 77, 's3': 90}

print(assignment_averages(students))
# Esperado:
# {'hw1': 82, 'hw2': 83, 'hw3': 92}