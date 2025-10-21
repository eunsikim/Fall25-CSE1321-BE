def avg(grade_list):
    sum = 0

    for grade in grade_list:
        sum += grade
    
    return sum / len(grade_list)

def calculate_grade(lab, assignment, midterm, final):
    return lab * 0.1 + assignment * 0.4 + midterm * 0.2 + final * 0.3

def main():
    student_list = [
        ["Alice", 80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89, 90, 100, 80, 81, 90, 100, 78, 90, 91],
        ["Bob", 80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89, 90, 100, 80, 81, 90, 100, 78, 90, 91],
        ["Charlie", 80, 91, 92, 87, 100, 70, 78, 80, 90, 100, 80, 60, 89, 90, 100, 80, 81, 90, 100, 78, 90, 91],
    ]

    for student in student_list:
        name = student[0]
        lab = avg(student[1:14])
        assignment = avg(student[14:21])
        midterm = student[21]
        final = student[22]

        final_grade = calculate_grade(lab, assignment, midterm, final)

        print(f"Student: {name}, Final Grade: {final_grade}")


if __name__ == "__main__":
    main()