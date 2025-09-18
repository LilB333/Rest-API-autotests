from utils.http_methods import Http_methods
from utils.base import Base

base = Base()
base_url = Base.base_url
endpoint = '/objects'

class PostObjects(Http_methods):

    def create_object(self, payload):
        self.response = Http_methods.post(base_url + endpoint, body=payload)
        response_json = self.response.json()
        print("При создании объекта получен ответ:\n", response_json)
        base.check_status_code(self.response)
        return response_json


class GetObjects(Http_methods):

    def get_all_objects(self):
        self.response = Http_methods.get(base_url + endpoint)
        response_json = self.response.json()
        return response_json

    def get_object_by_id(self, id):
        self.response = Http_methods.get(base_url + endpoint + "/" + id)
        response_json = self.response.json()
        print("При получении объекта по id получен ответ:\n", response_json)
        return response_json

class UpdateObjects(Http_methods):

    def update_object(self, id, payload):
        self.response = Http_methods.put(base_url + endpoint + "/" + id, body=payload)
        response_json = self.response.json()
        print("При изменении объекта получен ответ:\n", response_json)
        return response_json

    def partially_update_object(self, id, payload):
        self.response = Http_methods.patch(base_url + endpoint + "/" + id, body=payload)
        response_json = self.response.json()
        print("При частичном изменении объекта получен ответ:\n", response_json)
        return response_json

class DeleteObjects(Http_methods):
    def delete_object(self, id):
        self.response = Http_methods.delete(base_url + endpoint + "/" + id, body=None)
        response_json = self.response.json()
        print("При удалении объекта получен ответ:\n", response_json)
        return response_json