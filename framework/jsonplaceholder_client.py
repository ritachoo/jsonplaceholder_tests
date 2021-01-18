import allure
import requests as r

from typing import Dict, Optional
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _post(self, path: str, json_data: Optional):
        return r.post(url=JSONPLACEHOLDER_HOST + path, json=json_data)

    def _delete(self, path: str):
        return r.delete(url=JSONPLACEHOLDER_HOST + path)

    @allure.step
    def get_all_posts(self):
        return self._get(path='/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def get_post_by_user_id(self, user_id: int):
        return self._get(path=f'/posts?userId={user_id}')

    @allure.step
    def add_post(self, json_data: Optional[Dict]):
        return self._post('/posts', json_data)

    def delete_post(self, post_id: int):
        return self._delete(f'/posts/{post_id}')
