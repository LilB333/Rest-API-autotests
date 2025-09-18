class Base:
    base_url = "https://api.restful-api.dev"

    def check_status_code(self, response):
        assert response.status_code == 200
        print("Запрос успешен, статус код 200")