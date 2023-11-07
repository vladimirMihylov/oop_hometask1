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

    def __str__(self):
        return f"Имя: {self.name} \ Фамилия: {self.surname} \ Средняя оценка за домашние задания: {self.grades / len(self.grades)} \ Курсы в процессе изучения: {self.courses_in_progress} \ Завершенные курсы: {self.finished_courses}"

        
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
        return f"Имя : {self.name} \ Фамилия: {self.surname}"
 
class Reviewer(Mentor):
    pass

class Lecturer(Mentor):
    lecturer_grades = {}
    def rate_hw(self, student, course, grade):
        return f"Error: lecturer cannot review homework"
    
    def __str__(self):
        return f"Имя : {self.name} \ Фамилия: {self.surname} \ Средняя оценка за лекции: {self.lecturer_grades / len(lecturer_grades)}"

    