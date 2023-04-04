import requests

class Test_new_joke():
    """Створення нового жарту"""

    def __int__(self):
        pass

    def test_create_new_random_joke(self):
        """Створення випадкового жарту"""

        url = "https://api.chucknorris.io/jokes/random"
        print(url)
        result = requests.get(url)
        print("Статус код : " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Success!!! we got a new joke")
        else:
            print("Error!!! The request is invalid")
        result.encoding = 'utf-8'
        print(result.text)
        chuck = result.json()
        chuck_info = chuck.get("categories")
        print(chuck_info)
        assert chuck_info == []
        print("Category is correct")
        chuck_info_value = chuck.get("value")
        print(chuck_info_value)
        name = "Chuck"
        if name in chuck_info_value:
            print("Chuck is present")
        else:
            print("Chuck is missing")


random_joke = Test_new_joke()
random_joke.test_create_new_random_joke()