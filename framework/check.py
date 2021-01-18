import allure

from hamcrest import assert_that, equal_to, empty, has_entries
from typing import Dict
from requests import codes


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


@allure.step
def check_ok_response(response):
    _response_general_check(response)


@allure.step
def check_not_found_response(response):
    _response_general_check(response, codes.not_found)


@allure.step
def check_created_response(response):
    _response_general_check(response, codes.created)


@allure.step
def check_internal_server_error(response):
    _response_general_check(response, codes.internal_server_error)


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_post_by_id_response(response, post_id: int):
    _response_general_check(response)
    assert_that(response.json()['id'], equal_to(post_id))


@allure.step
def check_get_post_by_user_id_positive_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(10))


@allure.step
def check_get_post_by_user_id_negative_response(response):
    _response_general_check(response)
    assert_that(response.json(), empty())


@allure.step
def check_added_post_json_data(response, json_data: Dict):
    _response_general_check(response, codes.created)
    assert_that(response.json(),
                has_entries({'userId': json_data['userId'],
                             'title': json_data['title'],
                             'body': json_data['body']}))
