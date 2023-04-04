import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print("Статус код : "+ str(result.status_code))
assert 200 == result.status_code
if result.status_code == 200:
    print("Success!!! we got a new joke")
else:
    print("Error!!! The request is invalid")
result.encoding = 'utf-8'
print(result.text)
