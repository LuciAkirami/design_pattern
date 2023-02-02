class StudentDTO:
    def __init__(self,school,student_name):
        self.school = school
        self.student_name = student_name

    def getall(self):
        school = self.school
        students = list(self.student_name)
        return {"School": school, "Students":students}


    