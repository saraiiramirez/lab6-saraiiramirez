def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}

def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}
        
    name = input("Enter student name: ").strip().title()
    subject_grades = {}
    
    while True:
        entry = input("Enter subject and grade (or 'exit' to finish): ").strip()
        if entry.lower() == 'exit':
            break
        
        if ',' in entry:
            parts = entry.split(',')
            subject = parts[0].strip().title()
            grade = float(parts[1].strip())
            subject_grades[subject] = grade
            
    student_grades[name] = subject_grades
    print(f"Student {name} successfully added to the grades management system.")
    
    return student_grades

def get_students(student_grades, keys):
    result = {}
    lower_to_actual = {k.lower(): k for k in student_grades.keys()}
    
    for key in keys:
        lower_key = key.strip().lower()
        if lower_key in lower_to_actual:
            actual_name = lower_to_actual[lower_key]
            result[actual_name] = student_grades[actual_name]
        else:
            print(f"{key.strip().title()} not found!")
            
    return result

def avg_by_student(student_grades, keys=None):
    if keys is not None:
        target_students = get_students(student_grades, keys)
    else:
        target_students = student_grades
        
    for student, grades in target_students.items():
        if len(grades) > 0:
            avg = sum(grades.values()) / len(grades)
        else:
            avg = 0.0
        print(f"{student}: {avg:.1f}")