import requests
import json

if __name__ == '__main__':
    data = {'key': 'value'}

    r = requests.post('https://httpbin.org/post', json=json.dumps(
        data))  # отправляем POST-запрос, но только в этот раз тип передаваемых данных будет JSON
    print(r.content)
