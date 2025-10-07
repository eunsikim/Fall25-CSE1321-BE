def calc_avg(items_sum, items_size):
    return items_sum / items_size

def calc_weight(items_avg, item_weight):
    return items_avg * item_weight

def calc_grade(checkMax, lab1, lab2, lab3, lab4, lab5, assignment1, assignment2):
    if checkMax:
        labs_unknown = 800
        assignments_unknown = 500
        midterm_unknown = 100
        final_unknown = 100
    else:
        labs_unknown = 0
        assignments_unknown = 0
        midterm_unknown = 0
        final_unknown = 0

    labs_avg = calc_weight(calc_avg(lab1 + lab2 + lab3 + lab4 + lab5 + labs_unknown, 13), 0.1)
    assignments_avg = calc_weight(calc_avg(assignment1 + assignment2 + assignments_unknown, 7), 0.4)
    midterm_exam = calc_weight(midterm_unknown, 0.2)
    final_exam = calc_weight(final_unknown, 0.3)

    final_grade = labs_avg + assignments_avg + midterm_exam + final_exam

    return final_grade


def main():
    lab1 = float(input("Enter lab 1 grade: "))
    lab2 = float(input("Enter lab 2 grade: "))
    lab3 = float(input("Enter lab 3 grade: "))
    lab4 = float(input("Enter lab 4 grade: "))
    lab5 = float(input("Enter lab 5 grade: "))

    assignment1 = float(input("Enter assignment 1 grade: "))
    assignment2 = float(input("Enter assignment 2 grade: "))


    # 13 labs (10%), 7 assignments (40%), midterm (20%), final (30%)
    final_grade_max = calc_grade(True, lab1, lab2, lab3, lab4, lab5, assignment1, assignment2)
    print(f"Maximum grade possible: {final_grade_max:.2f}")

    final_grade_min = calc_grade(False, lab1, lab2, lab3, lab4, lab5, assignment1, assignment2)
    print(f"Minimum grade possible: {final_grade_min:.2f}")

    


if __name__ == "__main__":
    main()