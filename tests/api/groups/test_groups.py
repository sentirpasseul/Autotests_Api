import requests
from allure_commons.types import Severity

from services.university.group.helpers.group_helper import GroupHelper
from services.university.university_service import UniversityService
from utils.assertions.general_assertions import Assertions
from utils.responses.group_responses import GroupErrorResponses, GroupResponses
from utils.responses.user_responses import UserErrorsStrEnum
from utils.logs.allure_conf.allure_data import ParentSuit, Suit, SubSuit, Story, Feature, Label, Epic
from utils.logs.allure_conf.allure_config import allure_test_report


class TestGroups:
    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_VALID,
        feature=Feature.CREATE_GROUP,
        title="Create group - status code 201 (created)",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_create_group_status_code(self, group_helper, get_random_group):
        response = group_helper.post_group(get_random_group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_VALID,
        feature=Feature.CREATE_GROUP,
        title="Create group - correct message",
        severity=Severity.BLOCKER,
        label=Label.POSITIVE
    )
    def test_create_group_response(self, university_service, soft_assert, get_random_group):
        group = get_random_group
        response = university_service.create_group(group)
        soft_assert.check(response.name == group.name,
                          f'Group name mismatch: got {response.name}, expected {group.name}')

        soft_assert.assert_all()

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_GROUP,
        title="Create existed group - status code 409 (conflict)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_existed_group_status_code(self, group_helper, get_random_group):
        group = get_random_group
        group_helper.post_group(group.model_dump())
        response = group_helper.post_group(group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.conflict)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_GROUP,
        title="Create existed group - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_existed_group_response(self, university_service, get_random_group):
        group = get_random_group
        university_service.create_group(group)
        response = university_service.create_group(group)
        Assertions.validate_message(response, GroupErrorResponses.GROUP_IS_TAKEN)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_GROUP,
        title="Create group without credentials - status code 403 (forbidden)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_group_without_creds_status_code(self, university_api_utils_anonym, get_random_group):
        group_helper = GroupHelper(university_api_utils_anonym)
        group = get_random_group
        response = group_helper.post_group(group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_GROUP,
        title="Create group without credentials - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_group_without_creds_response(self, university_api_utils_anonym, get_random_group):
        university_service = UniversityService(university_api_utils_anonym)
        group = get_random_group
        response = university_service.create_group(group)
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_GROUP,
        title="Create group with fake token - status code 401 (unauthorized)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_group_with_fake_token_status_code(self, university_api_utils_fake_token, get_random_group):
        group_helper = GroupHelper(university_api_utils_fake_token)
        group = get_random_group
        response = group_helper.post_group(group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.CREATE_INVALID,
        feature=Feature.CREATE_GROUP,
        title="Create group with fake token - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_create_group_with_fake_token_response(self, university_api_utils_fake_token, get_random_group):
        university_service = UniversityService(university_api_utils_fake_token)
        group = get_random_group
        response = university_service.create_group(group)
        Assertions.validate_message(response, UserErrorsStrEnum.INVALID_JWT_TOKEN)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_VALID,
        feature=Feature.DELETE_GROUP,
        title="Delete group by group_id - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_delete_group_status_code(self, group_helper, university_api_utils, get_group_id):
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_VALID,
        feature=Feature.DELETE_GROUP,
        title="Delete group by group_id - correct message",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_delete_group_response(self, university_service, get_group_id):
        response = university_service.delete_group(get_group_id)
        Assertions.validate_message(response, GroupResponses.GROUP_DELETED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_INVALID,
        feature=Feature.DELETE_GROUP,
        title="Delete group without credentials - status code 403 (forbidden)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_delete_group_without_creds_status_code(self, university_api_utils_anonym, get_group_id):
        group_helper = GroupHelper(university_api_utils_anonym)
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.forbidden)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_INVALID,
        feature=Feature.DELETE_GROUP,
        title="Delete group without credentials - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_delete_group_without_creds_response(self, university_api_utils_anonym, get_group_id):
        university_service = UniversityService(university_api_utils_anonym)
        response = university_service.delete_grade(get_group_id)
        Assertions.validate_message(response, UserErrorsStrEnum.ACCESS_DENIED)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_INVALID,
        feature=Feature.DELETE_GROUP,
        title="Delete group with fake token - status code 401 (unauthorizaed)",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_delete_group_with_fake_token_status_code(self, university_api_utils_fake_token, get_group_id):
        group_helper = GroupHelper(university_api_utils_fake_token)
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.unauthorized)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_INVALID,
        feature=Feature.DELETE_GROUP,
        title="Delete group with fake token - correct error message",
        severity=Severity.CRITICAL,
        label=Label.NEGATIVE
    )
    def test_delete_group_with_fake_token_response(self, university_api_utils_fake_token, get_group_id):
        university_service = UniversityService(university_api_utils_fake_token)
        response = university_service.delete_group(get_group_id)
        Assertions.validate_message(response, UserErrorsStrEnum.INVALID_JWT_TOKEN)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_INVALID,
        feature=Feature.DELETE_GROUP,
        title="Delete non-existed group - status code 404 (not found)",
        severity=Severity.NORMAL,
        label=Label.NEGATIVE
    )
    def test_delete_group_not_existed_status_code(self, university_api_utils, get_group_id):
        group_helper = GroupHelper(university_api_utils)
        group_helper.delete_group_by_id(get_group_id)
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.not_found)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.DELETE_INVALID,
        feature=Feature.DELETE_GROUP,
        title="Delete non-existed group - correct error message",
        severity=Severity.NORMAL,
        label=Label.NEGATIVE
    )
    def test_delete_group_not_existed_response(self, university_api_utils, get_group_id):
        university_service = UniversityService(university_api_utils)
        university_service.delete_group(get_group_id)
        response = university_service.delete_group(get_group_id)
        Assertions.validate_message(response, GroupErrorResponses.GROUP_NOT_FOUND)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.GET_VALID,
        feature=Feature.GET_GROUPS,
        title="Get groups - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_groups(self, group_helper, university_api_utils):
        response = group_helper.get_groups()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.GET_VALID,
        feature=Feature.GET_GROUP,
        title="Get group by group_id - status code 200 (ok)",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_get_group_by_id(self, group_helper, university_api_utils, get_group_id):
        response = group_helper.get_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    @allure_test_report(
        parent_suit=ParentSuit.API,
        suit=Suit.SMOKE,
        sub_suit=SubSuit.GROUPS,
        epic=Epic.GROUPS,
        story=Story.UPDATE_PUT_VALID,
        feature=Feature.UPDATE_GROUP_PUT,
        title="Upgrade (put) group by group_id - status code (200) ok",
        severity=Severity.CRITICAL,
        label=Label.POSITIVE
    )
    def test_put_group_by_id(self, group_helper, university_api_utils, get_group_id, get_random_group):
        response = group_helper.put_group_by_id(group_id=get_group_id,
                                                json=get_random_group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)
