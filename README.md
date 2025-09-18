**Rest-API-autotests** - это проект автоматизированного тестирования API, предоставленного ресурсом **https://restful-api.dev/**.

## 🚀 Технологический стек

- **Python 3.11+** - язык программирования
- **Pytest** - фреймворк для тестирования
- **Requests** - для отправки HTTP-запросов к веб-сервисам и API
- **Allure Framework** - создание отчетов о тестировании
- **Pytest-ordering** - управление порядком выполнения тестов

## 📦 Установка и настройка

### Предварительные требования

1. Установите Python 3.11 или выше
2. Установите Git
3. Установите Allure

### Клонирование репозитория

```bash
git clone https://github.com/LilB333/Rest-API-autotests.git
cd Rest-API-autotests
```

### Создание виртуального окружения и активация

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

## 🏃 Запуск тестов

### Запуск всех тестов

```bash
pytest
```

### Запуск тестов с генерацией Allure отчетов

```bash
pytest --alluredir=allure-results
```

### Просмотр Allure отчета

```bash
allure serve allure-results
```

### Запуск конкретного тестового метода

```bash
pytest tests/test_objects.py::test_get_all_objects
```

## 🎯 Особенности реализации

### Использование json-схем для валидации данных

В файле schemas.py папки utils содержится описание схем для валидации данных. Валидация осуществляется с помощью библиотеки jsonschema путем сравнивания ответа со схемой:

```python
try:
   jsonschema.validate(instance=response_json, schema=schemas.get_all_objects)
   validation_passed = True
except jsonschema.ValidationError:
   validation_passed = False
assert validation_passed
print("Ответ API соответствует схеме")
```

### Управление порядком тестов

Тесты используют pytest-ordering для контроля последовательности выполнения:

```python
@pytest.mark.run(order=1)
```

### 📊 Отчетность

Проект использует Allure Framework для детальной отчетности:
- Графические отчеты о выполнении тестов
- Подробная информация о каждом шаге теста
- История выполнения тестов
  
## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте feature ветку (git checkout -b feature/amazing-feature)
3. Закоммитьте изменения (git commit -m 'Add amazing feature')
4. Запушьте ветку (git push origin feature/amazing-feature)
5. Откройте Pull Request
