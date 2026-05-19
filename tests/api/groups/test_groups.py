import requests

from utils.assertions.general_assertions import Assertions


class TestGroups:
    def test_create_group(self, group_helper, university_api_utils_anonym, generate_random_group):
        response = group_helper.post_group(generate_random_group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.created)

    def test_delete_group(self, group_helper, university_api_utils_anonym, get_group_id):
        response = group_helper.delete_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_groups(self, group_helper, university_api_utils_anonym):
        response = group_helper.get_groups()
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_get_group_by_id(self, group_helper, university_api_utils_anonym, get_group_id):
        response = group_helper.get_group_by_id(get_group_id)
        Assertions.validate_response_status_code(response, requests.codes.ok)

    def test_put_group_by_id(self, group_helper, university_api_utils_anonym, generate_random_group, get_group_id):
        response = group_helper.put_group_by_id(group_id=get_group_id,
                                                json=generate_random_group.model_dump())
        Assertions.validate_response_status_code(response, requests.codes.ok)
