from dao import StudentDAO
from dto import StudentDTO
# Create an instance of the DAO
student_dao = StudentDAO()

# Create a student variable
student1= "Lary"
student2 = "Mike"
school = "School:Hindenburg"

# Creating instances of DTO
stud1 = StudentDTO(school,student1)
stud2 = StudentDTO(school,student2)

# Add Student to the Database
student_dao.add_student(stud1)
student_dao.add_student(stud2)

# Retreiving data from the Database
student = student_dao.get_all_student("School:Hindenburg")
print(student)