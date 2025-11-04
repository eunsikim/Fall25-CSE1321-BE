def avg(grade_list):
    sum = 0

    lowest = min(grade_list)

    grade_list.remove(lowest)

    for grade in grade_list:
        sum += grade
    
    return sum / len(grade_list)

def main():
    pols1101_discussions = [90, 81, 70, 80, 100]
    pols1101_test1 = 80
    pols1101_test2 = 90
    pols1101_final_exam = 90
    pols1101_final_grade = avg(pols1101_discussions) * 0.25 + pols1101_test1 * 0.25 + pols1101_test2 * 0.25 + pols1101_final_exam * 0.25

    cse1321_quizzes = [80, 79, 90, 99, 100, 100, 84, 80, 95, 100]
    cse1321_test1 = 100
    cse1321_test2 = 100
    cse1321_final_exam = 90

    print(cse1321_quizzes)

    cse1321_final_grade = avg(cse1321_quizzes) * 0.25 + cse1321_test1 * 0.25 + cse1321_test2 * 0.25 + cse1321_final_exam * 0.25 

    # In American Politics I we do not drop the lowest discussion,
    # We get the incorrect final grade by calling the avg()
    print(f"American Politics I: {pols1101_final_grade}")
    print(f"Programming and Problem Solving I: {cse1321_final_grade}")


if __name__ == "__main__":
    main()