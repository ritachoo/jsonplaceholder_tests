import allure

from framework.check import check_get_post_by_user_id_positive_response, check_get_post_by_user_id_negative_response
from framework.helper import generate_random_id


@allure.suite('GET /posts/<post_id>?userId=<user_id>')
class TestGetPostByUserId:

    @allure.title('Positive. Get post by user id')
    def test_get_post_by_id_positive(self, client):
        user_id = generate_random_id(end=10)
        response = client.get_post_by_user_id(user_id)
        check_get_post_by_user_id_positive_response(response)

    @allure.title('Negative. Get post by user id')
    def test_get_post_by_id_negative(self, client):
        user_id = generate_random_id(11, 99)
        response = client.get_post_by_user_id(user_id)
        check_get_post_by_user_id_negative_response(response)
