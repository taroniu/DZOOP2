class Student:
    counter = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avarage_score = 0
        # Student.counter.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def mentor_rate(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'error'
        
    def avarage(self):
        scores_list = []
        for value in self.grades.values():
            scores_list.extend(value)
        self.avarage_score = sum(scores_list) / len(scores_list)
        print(f'Avarage score of student {self.surname} is {self.avarage_score}')

    def __str__(self):
        new_print = f'''Имя: {self.name}
Фамилия: {self.surname} 
Средняя оценка за домашние задания: {self.avarage_score} 
курсы в процессе изучения: {self.courses_in_progress} 
Завершенные курсы: {self.finished_courses}'''
        return new_print

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('the operand on the right must have the type Student')
        return self.avarage_score == other.avarage_score

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('the operand on the right must have the type Student')
        return self.avarage_score > other.avarage_score

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('the operand on the right must have the type Student')
        return self.avarage_score < other.avarage_score

    def __ne__(self, other):
        if not isinstance(other, Student):
            print('the operand on the right must have the type Student')
        return self.avarage_score != other.avarage_score

    def __le__(self, other):
        if not isinstance(other, Student):
            print('the operand on the right must have the type Student')
        return self.avarage_score <= other.avarage_score

    def __ge__(self, other):
        if not isinstance(other, Student):
            print('the operand on the right must have the type Student')
        return self.avarage_score >= other.avarage_score

    def avarage_grade_for_the_course(self, course):
        scores = []
        for i in self:
            if not isinstance(i, Student):
                print('all objects must be in the class Student')
            else:
                for key, value in i.grades.items():
                    if course == key:
                        scores.extend(value)
        scores = sum(scores) / len(scores)
        print(f'Средний балл у студенгов за курс {course} - {scores}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    counter = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avarage_score = 0
        Lecturer.counter.append(self)

    def avarage(self):
        scores_list = []
        for value in self.grades.values():
            scores_list.extend(value)
        self.avarage_score = sum(scores_list) / len(scores_list)
        print(f'Avarage score of lecturer {self.surname} is {self.avarage_score}')  

    def __str__(self):
                new_print = f'''Имя: {self.name}
Фамилия: {self.surname} 
Средняя оценка за лекции: {self.avarage_score}'''
                return new_print 

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('the operand on the right must have the type Lecturer')
        return self.avarage_score == other.avarage_score

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('the operand on the right must have the type Lecturer')
        return self.avarage_score > other.avarage_score

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('the operand on the right must have the type Lecturer')
        return self.avarage_score < other.avarage_score

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            print('the operand on the right must have the type Lecturer')
        return self.avarage_score != other.avarage_score

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('the operand on the right must have the type Lecturer')
        return self.avarage_score <= other.avarage_score

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print('the operand on the right must have the type Lecturer')
        return self.avarage_score >= other.avarage_score

    def avarage_grade_for_the_course(self, course):
        scores = []
        for i in self:
            if not isinstance(i, Lecturer):
                print('all objects must be in the class Lecturer')
            else:
                for key, value in i.grades.items():
                    if course == key:
                        scores.extend(value)
        scores = sum(scores) / len(scores)
        print(f'Средний балл у лекторов за курс {course} - {scores}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'
        
    def __str__(self):
        new_print = f"Имя: {self.name} \nФамилия: {self.surname}"
        return new_print
    

student1 = Student('Lionel', 'Messi', 'M')
student1.add_courses('Введение в программирование')
student1.courses_in_progress.append('Python')
student1.courses_in_progress.append('Git')

student2 = Student('Skrudg', 'Macduck', 'M')
student2.add_courses('Введение в программирование')
student2.courses_in_progress.append('Python')
student2.courses_in_progress.append('Git')

lecturer1 = Lecturer('Bill', 'Gates')
lecturer1.courses_attached.append('Python')
lecturer1.courses_attached.append('Git')

lecturer2 = Lecturer('Obivan', 'Dartvader')
lecturer2.courses_attached.append('Python')
lecturer2.courses_attached.append('Git')

student1.mentor_rate(lecturer1, 'Python', 9) # оценки лектораам
student1.mentor_rate(lecturer1, 'Git', 8)
student2.mentor_rate(lecturer2, 'Python', 8)
student2.mentor_rate(lecturer2, 'Git', 10)

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached = ['Python', 'Git']
some_reviewer.rate_hw(student1, 'Python', 8) # оценки студентам
some_reviewer.rate_hw(student1, 'Git', 9)
some_reviewer.rate_hw(student2, 'Git', 7)
some_reviewer.rate_hw(student2, 'Python', 9)


print('средний балл____-__________')
student1.avarage() # средний балл
student2.avarage()
lecturer1.avarage()
lecturer2.avarage()          

print()
print('средний балл за курс____________________________')
stud_list = [student1, student2]
lecturer_list = [lecturer1, lecturer2]
Student.avarage_grade_for_the_course(stud_list, 'Git') # подсчет средней оценки за ДЗ по всем студентам/лекторам в рамках конкретного курса
Student.avarage_grade_for_the_course(stud_list, 'Python')
Lecturer.avarage_grade_for_the_course(lecturer_list, 'Python')
Lecturer.avarage_grade_for_the_course(lecturer_list, 'Git')

print() # Перегрузка __str__ у всех классов
print('перегрузка __str__ ____________')
print(student1)
print(lecturer1)
print(some_reviewer)

print()
print('сравнение средних баллов у студентов/лекторов----------------')

print(student2.__ne__(student1))
print(student1.__eq__(student2))
print(student1.__gt__(student2))
print(student1.__le__(student2))
print(student1.__lt__(student2))
print(student1.__ge__(student2))
print(student1 == student2)


