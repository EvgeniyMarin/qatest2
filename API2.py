import requests

class new_joke():

    def __init__(self):
        pass

    def joke_category(self):
        url_category = 'https://api.chucknorris.io/jokes/categories'
        full_category = requests.get(url_category)                                                                # выполняем GET запрос для получения категорий шуток
        print('Список категорий шуток:', full_category.text)
        users_category = ''
        full_category_json = full_category.json()                                                                 # записываем в переменную список категорий шуток в json
        url = 'https://api.chucknorris.io/jokes/random?category='
        while users_category != 'exit':                                                                           # программа будет принимать запросы пока пользователь не введет exit
            users_category = input('Введите категорию из списка выше (Для завершения программы введите exit): ')
            if users_category == 'exit':
                break
            if users_category in full_category_json:
                print(f'Выбрана категория: "{users_category }" она есть в списке!')
                result = requests.get(url + users_category)                                                       # записываем в переменную результат запроса GET с корректной категорией шуток
                print(url + users_category)
                print(f'Статус код: {result.status_code}')
                assert result.status_code == 200
                joke = result.json()
                print('Вы получили шутку:')
                print(joke.get('value'))
            else:
                result = requests.get(url + users_category)
                print(f'Статус код: {result.status_code}')
                print('НЕТ ТАКОЙ КАТЕГОРИИ ШУТОК')


joke = new_joke()
joke.joke_category()

