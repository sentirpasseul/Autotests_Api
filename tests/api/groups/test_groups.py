from http.client import responses

import requests

from services.university.group.helpers.group_helper import GroupHelper
from services.university.university_service import UniversityService
from utils.assertions.general_assertions import Assertions
from conftest import generate_random_group
from utils.responses.general_responses import GeneralErrors
from utils.responses.group_responses import GroupErrorResponses, GroupResponses
from utils.responses.user_responses import UserErrorsStrEnum


class TestGroups:
    def test_create_group_status_code(self, group_helper):
        response = group_helper.post_group(generate_random_group().model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_create_group_response(self, university_service, soft_assert):
        group = generate_random_group()
        response = university_service.create_group(group)
        soft_assert.check(response.name == group.name,
                          f'Group name mismatch: got {response.name}, expected {group.name}')
        soft_assert.assert_all()

    def test_create_existed_group_status_code(self, group_helper):
        group = generate_random_group()
        group_helper.post_group(group.model_dump())
        response = group_helper.post_group(group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.conflict)

    def test_create_existed_group_response(self, university_service):
        group = generate_random_group()
        university_service.create_group(group)
        response = university_service.create_group(group)
        Assertions.validate_message(response, GroupErrorResponses.GROUP_IS_TAKEN)

    def test_create_group_without_creds_status_code(self, university_api_utils_anonym):
        group_helper = GroupHelper(university_api_utils_anonym)
        group = generate_random_group()
        response = group_helper.post_group(group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_create_group_without_creds_response(self, university_api_utils_anonym):
        university_service = UniversityService(university_api_utils_anonym)
        group = generate_random_group()
        response = university_service.create_group(group)
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    def test_create_group_with_fake_token_status_code(self, university_api_utils_fake_token):
        group_helper = GroupHelper(university_api_utils_fake_token)
        group = generate_random_group()
        response = group_helper.post_group(group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_create_group_with_fake_token_response(self, university_api_utils_fake_token):
        university_service = UniversityService(university_api_utils_fake_token)
        group = generate_random_group()
        response = university_service.create_group(group)
        Assertions.validate_message(response, UserErrorsStrEnum.INVALID_JWT_TOKEN)

    def test_delete_group_status_code(self, group_helper, university_api_utils, get_group_id):
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_delete_group_response(self, university_service, get_group_id):
        response = university_service.delete_group(get_group_id)
        Assertions.validate_message(response, GroupResponses.GROUP_DELETED)

    def test_delete_group_without_creds_status_code(self, university_api_utils_anonym, get_group_id):
        group_helper = GroupHelper(university_api_utils_anonym)
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    def test_delete_group_without_creds_response(self, university_api_utils_anonym, get_group_id):
        university_service = UniversityService(university_api_utils_anonym)
        response = university_service.delete_grade(get_group_id)
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    def test_delete_group_with_fake_token_status_code(self, university_api_utils_fake_token, get_group_id):
        group_helper = GroupHelper(university_api_utils_fake_token)
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    def test_delete_group_with_fake_token_response(self, university_api_utils_fake_token, get_group_id):
        university_service = UniversityService(university_api_utils_fake_token)
        response = university_service.delete_group(get_group_id)
        Assertions.validate_message(response, UserErrorsStrEnum.INVALID_JWT_TOKEN)

    def test_delete_group_not_existed_status_code(self, university_api_utils, get_group_id):
        group_helper = GroupHelper(university_api_utils)
        group_helper.delete_group_by_id(get_group_id)
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.not_found)

    def test_delete_group_not_existed_response(self, university_api_utils, get_group_id):
        university_service = UniversityService(university_api_utils)
        university_service.delete_group(get_group_id)
        response = university_service.delete_group(get_group_id)
        Assertions.validate_message(response, GroupErrorResponses.GROUP_NOT_FOUND)

    def test_get_groups(self, group_helper, university_api_utils):
        response = group_helper.get_groups()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_group_by_id(self, group_helper, university_api_utils, get_group_id):
        response = group_helper.get_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_group_by_id(self, group_helper, university_api_utils, get_group_id):
        response = group_helper.put_group_by_id(group_id=get_group_id,
                                                json=generate_random_group().model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)
