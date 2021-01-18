import allure
import pytest

from framework.check import check_ok_response


@allure.suite('DELETE /posts/<post_id>')
class TestDeletePost:

    @allure.title('Positive. Delete post')
    @pytest.mark.parametrize("post_id", list(range(1, 5)))
    def test_delete_post(self, client, post_id):
        response = client.delete_post(post_id)
        check_ok_response(response)
