class Course_Manager:
    def __init__(self):
        self.course_list = []

    def print_courses(self):
        for i in range(len(self.course_list)):
            print(f"{i} - {self.course_list[i].name} - {self.course_list[i].day} - {self.course_list[i].time} at {self.course_list[i].location}")