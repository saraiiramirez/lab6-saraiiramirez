def student_averages(students):
    result = {}

    for student, grades in students.item():
        total = sum(grades.values())
        count = len(grades)
        average = round(total / count)
        result[student] = average

    return result

def assigment_averages(students):
    result = {}

    for student, grades in students.items():
        for assignment, score in grades.items():
            if assignment in result:
                result[assignment].append(score)

    for assignment in result:
        avg = round(sum(result[assignment]) / len(result[assignment]))
        result[assignment] = avg


