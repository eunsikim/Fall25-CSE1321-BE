class pols1101:
    def __init__ (self, discussions, t1, t2, final_exam):
        self.discussion = discussions
        self.test1 = t1
        self.test2 = t2
        self.final_exam = final_exam
    
    def avg(self):
        sum = 0

        for grade in self.discussion:
            sum += grade
        
        return sum / len(self.discussion)

    def get_final_grade(self):
        return self.avg() * 0.25 + self.test1 * 0.25 + self.test2 * 0.25 + self.final_exam * 0.25

class cse1321:
    def __init__ (self, quizzes, t1, t2, final_exam):
        self.quizzes = quizzes
        self.test1 = t1
        self.test2 = t2
        self.final_exam = final_exam
    
    def avg(self):
        sum = 0

        lowest = min(self.quizzes)

        self.quizzes.remove(lowest)

        for grade in self.quizzes:
            sum += grade
        
        return sum / len(self.quizzes)

    def get_final_grade(self):
        return self.avg() * 0.25 + self.test1 * 0.25 + self.test2 * 0.25 + self.final_exam * 0.25
    
def main():
    AmGov1 = pols1101([90, 81, 70, 80, 100], 80, 90, 90)
    Prog1 = cse1321([80, 79, 90, 99, 100, 100, 84, 80, 95, 100], 100, 100, 90)

    print(f"American Politics I: {AmGov1.get_final_grade()}")
    print(f"Programming and Problem Solving I: {Prog1.get_final_grade()}")

if __name__ == "__main__":
    main()