from utils.assertions.student_assertions import StudentAssertions


class TestStudent:
    def test_create_student(self, generate_random_student, university_service):
        student = generate_random_student
        response = university_service.create_student(student)
        StudentAssertions.check_student_data(actual=student, expected=response)



