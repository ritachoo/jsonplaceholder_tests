import allure
import json

from framework.check import check_created_response, check_internal_server_error
from framework.helper import generate_json_data


@allure.suite('POST /posts')
class TestAddPost:

    @allure.title('Positive. Add post')
    def test_add_post_positive(self, client):
        json_data = generate_json_data()
        response = client.add_post(json_data)
        check_created_response(response)

    @allure.title('Negative. Add post')
    def test_add_post_negative(self, client):
        response = client.add_post(json.dumps(123))
        check_internal_server_error(response)
