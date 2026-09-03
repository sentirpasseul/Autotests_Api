from faker import Faker
import jwt
import datetime
import random
import uuid

from services.authorization.models.register_request import RegisterRequest
from services.university.grade.models.grade import GradeRequest
from services.university.group.models.group_request import GroupRequest
from services.university.group.models.subjects import Subjects
from services.university.student.models.student import DegreeEnum
from services.university.student.models.student_request import StudentRequest
from services.university.teacher.models.teacher_request import TeacherRequest
from utils.logs.logger.logger import Logger



class FactoryRandomData:
    faker = Faker()
    ALLOWED_SPECIAL_CHARS = '!"#$%&\'()*+,-./:;<=>?@^_`{|}~[]'
    MIN_GRADE = 0
    MAX_GRADE = 5

    @staticmethod
    def generate_hash():
        return uuid.uuid4().hex[:8]

    @staticmethod
    def generate_unique_username_with_hash():
        username = FactoryRandomData.faker.unique.user_name()
        suffix = FactoryRandomData.generate_hash()
        return f"{username}_{suffix}"

    @staticmethod
    def generate_unique_email_with_hash():
        email = FactoryRandomData.generate_unique_username_with_hash()
        return f"{email}@test.com"

    @staticmethod
    def generate_random_password():
        password = FactoryRandomData.faker.password(length=30,
                                                    special_chars=True,
                                                    digits=True,
                                                    upper_case=True,
                                                    lower_case=True)
        return password

    @staticmethod
    def generate_jwt_token():
        payload = {
            "sub": FactoryRandomData.faker.uuid4(),
            "name": FactoryRandomData.faker.name(),
            "email": FactoryRandomData.faker.email(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        secret = "test_secret"
        return jwt.encode(payload, secret, algorithm="HS256")

    @staticmethod
    def get_random_grade():
        return random.randrange(start=FactoryRandomData.MIN_GRADE, stop=FactoryRandomData.MAX_GRADE+1)


    @staticmethod
    def generate_random_user():
        username = FactoryRandomData.generate_unique_username_with_hash()
        password = FactoryRandomData.generate_random_password()
        email = FactoryRandomData.generate_unique_email_with_hash()
        user_data = {
            "username": username,
            "password": password,
            "password_repeat": password,
            "email": email
        }
        log_data = user_data.copy()
        Logger.info(f"Generated user: {log_data}")
        return RegisterRequest(**user_data)

    @staticmethod
    def generate_random_group():
        group = GroupRequest(name=FactoryRandomData().faker.bothify("???-##-#"))
        Logger.info(f"Generated group: {group}")
        return group

    @staticmethod
    def generate_random_student(group_id: int):
        student = StudentRequest(first_name=FactoryRandomData().faker.first_name(),
                                 last_name=FactoryRandomData().faker.last_name(),
                                 email=FactoryRandomData().faker.email(),
                                 degree=random.choice([option for option in DegreeEnum]),
                                 phone=FactoryRandomData().faker.numerify("+7##########"),
                                 group_id=group_id)
        Logger.info(f"Generated student: {student}")
        return student

    @staticmethod
    def generate_random_teacher():
        teacher = {
            "first_name": FactoryRandomData().faker.first_name(),
            "last_name": FactoryRandomData().faker.last_name(),
            "subject": random.choice(list(Subjects))
        }
        Logger.info(f"Generated teacher: {teacher}")
        return TeacherRequest(**teacher)

    @staticmethod
    def generate_random_grade(teacher_id, student_id):
        grade = {
            "teacher_id": teacher_id,
            "student_id": student_id,
            "grade": FactoryRandomData.get_random_grade()
        }
        Logger.info(f"Generated grade: {grade}")
        return GradeRequest(**grade)
