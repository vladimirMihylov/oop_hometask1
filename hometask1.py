class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades and 1 < grade < 10:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Error: no grades'
        else:
            return round(mid_sum / len(self.grades.values()), 2)

    def average_course_grade(self, course):
        if course in self.grades:
            return round(sum(self.grades[course]) / len(self.grades[course]), 2)
        else:
            return f'Error: no grades'

    def __lt__(self, other):
      if isinstance(other, Student):
        return self.average_grade() < other.average_grade()
      else:
        return 'Error'

    def __gt__(self, other):
      if isinstance(other, Student):
        return self.average_grade() > other.average_grade()
      else:
        return 'Error'


    def __eq__(self, other):
      if isinstance(other, Student):
        return self.average_grade() == other.average_grade()
      else:
        return 'Error'

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}"

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя : {self.name} \nФамилия: {self.surname}"
 
class Reviewer(Mentor):
    pass

class Lecturer(Mentor):
    lecturer_grades = {}
    def rate_hw(self, student, course, grade):
        return f"Error: lecturer cannot review homework"

    def average_grade(self):
        mid_sum = 0
        for course_grades in self.lecturer_grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Error: no grades'
        else:
            return round(mid_sum / len(self.lecturer_grades.values()), 2)

    def average_course_grade(self, course):
        if course in self.lecturer_grades:
            return round(sum(self.lecturer_grades[course]) / len(self.lecturer_grades[course]), 2)
        else:
            return f'Error: no grades'

    def __lt__(self, other):
      if isinstance(other, Lecturer):
        return self.average_grade() < other.average_grade()
      else:
        return 'Error'

    def __gt__(self, other):
      if isinstance(other, Lecturer):
        return self.average_grade() > other.average_grade()
      else:
        return 'Error'


    def __eq__(self, other):
      if isinstance(other, Lecturer):
        return self.average_grade() == other.average_grade()
      else:
        return 'Error'
    
    def __str__(self):
        return f"Имя : {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}"

some_student = Student('Ruoy', 'Eman', 'male')
other_student = Student('Ivan', 'Ivanov', 'male')

some_lecturer = Lecturer('Some', 'Buddy')
other_lecturer = Lecturer('Other', 'Buddy')

some_reviewer = Reviewer('Some', 'Reviewer')
other_reviewer = Reviewer('Other', 'Reviewer')

some_student.courses_in_progress += 'Python', 'Git', 'Java'
other_student.courses_in_progress += 'JS', 'Git', 'Java'

some_lecturer.courses_attached += 'Python', 'Git', 'Java'
other_lecturer.courses_attached += 'JS', 'Git', 'Java'

some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Git', 9)
some_student.rate_lecturer(some_lecturer, 'Java', 8)

other_student.rate_lecturer(other_lecturer, 'JS', 10)
other_student.rate_lecturer(other_lecturer, 'Git', 4)
other_student.rate_lecturer(other_lecturer, 'Java', 7)

some_reviewer.courses_attached += 'Python', 'Git', 'Java'
other_reviewer.courses_attached += 'JS', 'Git', 'Java'

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer.rate_hw(some_student, 'Java', 8)

other_reviewer.rate_hw(other_student, 'JS', 10)
other_reviewer.rate_hw(other_student, 'Git', 4)
other_reviewer.rate_hw(other_student, 'Java', 7)

print(some_student)
print(some_lecturer)
print(other_student)
print(other_lecturer)

print(some_student < other_student)
print(some_student > other_student)
print(some_student == other_student)

print(some_lecturer < other_lecturer)
print(some_lecturer > other_lecturer)
print(some_lecturer == other_lecturer)


# Задача 4 (Доработка) 

print(some_student.average_course_grade('Python'))
print(other_student.average_course_grade('Git'))

print(some_lecturer.average_course_grade('Python'))
print(other_lecturer.average_course_grade('Git'))

# Задача 4 вар 2

students_list = [some_student, other_student]
lecturers_list = [some_lecturer, other_lecturer]
def average_course_student_grade(students_list, course_name):
    sum_grades = 0
    count_grades = 0
    for student in students_list:
        if course_name in student.grades:
            sum_grades += sum(student.grades[course_name])
            count_grades += len(student.grades[course_name])
    if count_grades == 0:
        return f'Error: no grades'
    else:
        return round(sum_grades / count_grades, 2)

def average_course_lector_grade(lecturers_list, course_name):
    sum_grades = 0
    count_grades = 0
    for lector in lecturers_list:
        if course_name in lector.lecturer_grades:
            sum_grades += sum(lector.lecturer_grades[course_name])
            count_grades += len(lector.lecturer_grades[course_name])
    if count_grades == 0:
        return f'Error: no grades'
    else:
        return round(sum_grades / count_grades, 2)

print(average_course_student_grade(students_list, 'Python'))
print(average_course_lector_grade(lecturers_list, 'Python'))