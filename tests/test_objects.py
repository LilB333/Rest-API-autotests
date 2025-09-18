import copy
import allure
import jsonschema
import pytest
from utils import schemas
from utils.api import UpdateObjects, DeleteObjects
from utils.api import GetObjects

"ТЕСТ: ПОЛУЧЕНИЕ ВСЕХ ОБЪЕКТОВ"
@pytest.mark.run(order=1)
@allure.description("Test get all objects")
def test_get_all_objects():
    response = GetObjects()
    response_json = response.get_all_objects()
    # Проверяем что полученный ответ соответствует jsonschema
    try:
        jsonschema.validate(instance=response_json, schema=schemas.get_all_objects)
        validation_passed = True
    except jsonschema.ValidationError:
        validation_passed = False
    assert validation_passed
    print("Ответ API соответствует схеме")

"ТЕСТ: СОЗДАНИЕ ОБЪЕКТА"
@pytest.mark.run(order=2)
@allure.description("Test add object")
def test_add_object(create_object):
    # Получаем json-ответ созданного объекта
    new_object = create_object[0]
    try:
        jsonschema.validate(instance=new_object, schema=schemas.post_object)
        validation_passed = True
    except jsonschema.ValidationError:
        validation_passed = False
    assert validation_passed
    print("Добавленный объект соответствует схеме")

"ТЕСТ: ПОЛУЧЕНИЕ СОЗДАННОГО ОБЪЕКТА"
@pytest.mark.run(order=3)
@allure.description("Test get new object")
def test_get_new_object(create_object):
    # Получаем id объекта и его json-ответ
    new_object, payload = create_object
    object_id = new_object["id"]
    response = GetObjects()
    # Получаем json-ответ для объекта с заданным id
    response_json = response.get_object_by_id(object_id)
    # Создаем переменную для проверки созданного объекта
    created_object_json = {"id": object_id, **payload}
    # Проверяем что полученный объект идентичен ранее созданному
    assert response_json == created_object_json
    print("Полученный объект соответствует созданному")

"ТЕСТ: ОБНОВЛЕНИЕ СОЗДАННОГО ОБЪЕКТА"
@pytest.mark.run(order=4)
@allure.description("Test update new object")
def test_update_new_object(create_object):
    # Получаем id объекта и его json-ответ
    new_object, payload = create_object
    object_id = new_object["id"]
    response = GetObjects()
    # Получаем json-ответ для объекта с заданным id
    response_json = response.get_object_by_id(object_id)
    # Создаем переменную для проверки созданного объекта
    created_object_json = {"id": object_id, **payload}
    # Проверяем что полученный объект идентичен ранее созданному
    assert response_json == created_object_json
    print("Полученный объект соответствует созданному")
    # Копируем Добавляем новое поле
    updated_json = copy.deepcopy(payload)
    updated_json["data"]["color"] = "pink"
    response = UpdateObjects()
    update_object = response.update_object(object_id, updated_json)
    assert update_object["data"]["color"] == "pink"
    print("Поле успешно добавлено в объект")

"ТЕСТ: ЧАСТИЧНОЕ ОБНОВЛЕНИЕ СОЗДАННОГО ОБЪЕКТА"
@pytest.mark.run(order=5)
@allure.description("Test partially update new object")
def test_partially_update_new_object(create_object):
    # Получаем id объекта и его json-ответ
    new_object, payload = create_object
    object_id = new_object["id"]
    response = GetObjects()
    # Получаем json-ответ для объекта с заданным id
    response_json = response.get_object_by_id(object_id)
    # Создаем переменную для проверки созданного объекта
    created_object_json = {"id": object_id, **payload}
    # Проверяем что полученный объект идентичен ранее созданному
    assert response_json == created_object_json
    print("Полученный объект соответствует созданному")
    # Добавляем новое поле
    updated_json = {"name": "Updated 2025 GOAT Apple MacBook Pro 16"}
    response = UpdateObjects()
    update_object = response.partially_update_object(object_id, updated_json)
    assert update_object["name"] == "Updated 2025 GOAT Apple MacBook Pro 16"
    print(f"Поле успешно изменено на {updated_json}")

"ТЕСТ: УДАЛЕНИЕ СОЗДАННОГО ОБЪЕКТА"
@pytest.mark.run(order=6)
@allure.description("Test delete new object")
def test_delete_new_object(create_object):
    # Получаем id объекта и его json-ответ
    new_object, payload = create_object
    object_id = new_object["id"]
    response = GetObjects()
    # Получаем json-ответ для объекта с заданным id
    response_json = response.get_object_by_id(object_id)
    # Создаем переменную для проверки созданного объекта
    created_object_json = {"id": object_id, **payload}
    # Проверяем что полученный объект идентичен ранее созданному
    assert response_json == created_object_json
    print("Полученный объект соответствует созданному")
    response = DeleteObjects()
    response_json = response.delete_object(object_id)
    assert response_json == {"message": f"Object with id = {object_id} has been deleted."}
    print(f"Сообщение об удалении объекта с id='{object_id}' верное")

