def avg(grade_list):
    sum = 0

    for grade in grade_list:
        sum += grade
    
    return sum / len(grade_list)

def calculate_grade(lab, assignment, midterm, final):
    return lab * 0.1 + assignment * 0.4 + midterm * 0.2 + final * 0.3

def main():
    student_dictionary = {
        "Alice": {
            "Lab": [80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89],
            "Assignment": [90, 100, 80, 81, 90, 100, 78],
            "Midterm_Exam": 90,
            "Final_Exam": 91
        },
        "Bob": {
            "Lab": [80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89],
            "Assignment": [90, 100, 80, 81, 90, 100, 78],
            "Midterm_Exam": 90,
            "Final_Exam": 91
        },
        "Charlie": {
            "Lab": [80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89],
            "Assignment": [90, 100, 80, 81, 90, 100, 78],
            "Midterm_Exam": 90,
            "Final_Exam": 91
        }
    }

    for student in student_dictionary:
        name = student
        lab = avg(student_dictionary[student]["Lab"])
        assignment = avg(student_dictionary[student]["Assignment"])
        midterm = student_dictionary[student]["Midterm_Exam"]
        final = student_dictionary[student]["Final_Exam"]

        final_grade = calculate_grade(lab, assignment, midterm, final)

        print(f"Student: {name}, Final Grade: {final_grade}")

    print()
    
    search = input("Enter Student Name: ")

    print(f"Student {search}")
    print(f"Labs: {student_dictionary[search]["Lab"]}")
    print(f"Assignment: {student_dictionary[search]["Assignment"]}")
    print(f"Midterm Exam: {student_dictionary[search]["Midterm_Exam"]}")
    print(f"Final Exam: {student_dictionary[search]["Final_Exam"]}")



if __name__ == "__main__":
    main()