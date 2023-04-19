import requests

token = ''

def get_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(token)
    }

def request_status_get():
    headers = get_headers()
    url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f'\nКод ответа соответствует 200')
        return response.status_code


def request_status_new_folder(name_path):
    headers = get_headers()
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {"path": name_path, 'overwrite': 'true'}
    response = requests.put(url, headers=headers, params=params)
    if response.status_code != 201:
        print(f'Папка с именем: {name_path} уже существует!')
        return(response.status_code)
    else:
        print(f'\nКод ответа соответствует 201 \nПапка: {name_path} появилась в списке файлов')
        return response.status_code

