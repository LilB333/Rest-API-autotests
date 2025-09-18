import pytest
from utils import data_payload
from utils.api import PostObjects

"Cоздаем параметризованную фикстуру, которая создает объект с заданным payload"
@pytest.fixture(params= [data_payload.payload_1, data_payload.payload_2, data_payload.payload_3])
def create_object(request):
    response = PostObjects()
    payload = request.param
    "Создаем объект с заданными в body данными"
    new_object = response.create_object(payload)
    "Возвращаем созданный объект и json-ответ для получения объекта"
    return new_object, payload