from faker import Faker
import jwt
import datetime


class FactoryRandomData:
    faker = Faker()

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
