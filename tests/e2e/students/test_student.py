from utils.assertions.student_assertions import StudentAssertions


class TestStudent:
    def test_create_student(self, generate_random_student, university_service):
        response = university_service.create_student(generate_random_student)
        StudentAssertions.check_student_data(actual=generate_random_student, expected=response)
