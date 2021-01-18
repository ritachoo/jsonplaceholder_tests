import allure

from framework.check import check_get_all_posts_response


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self, client):
        response = client.get_all_posts()
        check_get_all_posts_response(response)
