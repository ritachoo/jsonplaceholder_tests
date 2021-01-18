import allure

from framework.check import check_get_post_by_id_response, check_not_found_response
from framework.helper import generate_random_id


@allure.suite('GET /posts/<post_id>')
class TestGetPostById:

    @allure.title('Positive. Get post by id')
    def test_get_post_by_id_positive(self, client):
        post_id = generate_random_id()
        response = client.get_post_by_id(post_id)
        check_get_post_by_id_response(response, post_id)

    @allure.title('Negative. Get post by id')
    def test_get_post_by_id_negative(self, client):
        post_id = generate_random_id(101, 999)
        response = client.get_post_by_id(post_id)
        check_not_found_response(response)
