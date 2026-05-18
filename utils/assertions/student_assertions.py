from services.university.student.models.student_request import StudentRequest
from services.university.student.models.student_response import StudentResponse


class StudentAssertions:

    @staticmethod
    def check_student_data(actual: StudentRequest, expected: StudentResponse):
        assert actual.first_name == expected.first_name, \
            f"First name mismatch: got {actual.first_name}, expected {expected.first_name}"
        assert actual.last_name == expected.last_name, \
            f"Last name mismatch: got {actual.last_name}, expected {expected.last_name}"
        assert actual.email == expected.email, \
            f"Email mismatch: got {actual.email}, expected {expected.email}"
        assert actual.degree == expected.degree, \
            f"Degree mismatch: got {actual.degree}, expected {expected.degree}"
        assert actual.phone == expected.phone, \
            f"Phone mismatch: got {actual.phone}, expected {expected.phone}"
        assert actual.group_id == expected.group_id, \
            f"Group id mismatch: got {actual.group_id}, expected {expected.group_id}"
