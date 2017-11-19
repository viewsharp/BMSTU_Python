from base_client import BaseClient
from json import loads


class Friends(BaseClient):
    # метод vk api
    method = "friends.get"
    # GET, POST, ...
    http_method = "GET"

    def __init__(self, user_id):
        self._user_id = user_id

    def get_params(self):
        return 'user_id={0}&fields=bdate'.format(self._user_id)

    def response_handler(self, response):
        return loads(response.text)['response']
