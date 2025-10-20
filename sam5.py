def add_student(students, name, grades):
    students[name] = tuple(grades)
    return students

def get_top_students(students, subject_index):
    sorted_students = sorted(students.items(), key=lambda x: x[1][subject_index], reverse=True)
    return tuple([name for name, grades in sorted_students[:3]])

students_dict = {}
add_student(students_dict, "Иван", [5, 4, 5, 3])
add_student(students_dict, "Мария", [4, 5, 5, 5])
add_student(students_dict, "Петр", [3, 4, 4, 4])

print("Топ студентов по математике:", get_top_students(students_dict, 0))
print("Топ студентов по физике:", get_top_students(students_dict, 1))