from base_client import BaseClient
from json import loads


class UserId(BaseClient):
    # метод vk api
    method = "users.get"
    # GET, POST, ...
    http_method = "GET"

    def __init__(self, username):
        self._username = username

    def get_params(self):
        return 'uids=' + self._username

    def response_handler(self, response):
        data = loads(response.text)['response']
        return data[0].get('uid')
