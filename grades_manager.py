def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}


def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    name = input("Enter student name: ").title()

    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ")
        if entry.lower() == "exit":
            break

        subject, grade = entry.split(",")
        subject = subject.strip().title()
        grade = float(grade.strip())

        subjects[subject] = grade

    student_grades[name] = subjects

    print(f"Student {name} successfully added to the grades management system.")

    return student_grades


def get_students(student_grades, keys):
    result = {}

    for name in keys:
        formatted_name = name.title()

        found = False
        for student in student_grades:
            if student.lower() == name.lower():
                result[student] = student_grades[student]
                found = True
                break

        if not found:
            print(f"{formatted_name} not found!")

    return result


def avg_by_student(student_grades, keys=None):
    if keys is None:
        data = student_grades
    else:
        data = get_students(student_grades, keys)

    for student, subjects in data.items():
        if subjects:
            avg = sum(subjects.values()) / len(subjects)
            print(f"{student}: {avg:.1f}")