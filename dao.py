import redis
from dto import StudentDTO

class StudentDAO:
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, decode_responses=True)

    def add_student(self, student_dto):
        self.client.sadd(student_dto.school,student_dto.student_name)

    def get_all_student(self, school):
        data = self.client.smembers(school)
        return StudentDTO(school,data).getall()
