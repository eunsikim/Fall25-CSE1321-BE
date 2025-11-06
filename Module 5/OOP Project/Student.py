import Grades as g
class Student:
    def __init__(self, id, password, name):
        self.id = id
        self.password = password
        self.name = name
        self.major = ""

        self.courses = [] # List of Course objs
        self.grades = [] # List of Grade objs
    
    def print_schedule(self):
        for course in self.course:
            print(f"{course.name} - {course.day} - {course.time} at {course.location}")
    
    def register(self, course_manager):
        course_manager.print_courses()
        option = input("Enter an index: ")

        # TODO: Implement the schedule conflict logic

        course_to_register = course_manager.course_list[option]

        self.courses.append(course_to_register)

        new_grade_obj = g.Grade(self, course_to_register)

        self.grades.append(new_grade_obj)

    def print_grades(self):
        for i in range(len(self.courses)):
            print(f"{self.courses[i]}: {self.grades[i]}")
