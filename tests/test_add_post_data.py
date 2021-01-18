import allure

from framework.check import check_added_post_json_data
from framework.helper import generate_json_data


@allure.suite('POST /posts')
class TestAddedPostJsonData:

    @allure.title('Positive. Add post')
    def test_added_post_json_data(self, client):
        json_data = generate_json_data()
        response = client.add_post(json_data)
        check_added_post_json_data(response, json_data)
