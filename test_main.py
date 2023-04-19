from unittest import TestCase
from main import geo_log, ids, stats_public
from yandex import request_status_get, request_status_new_folder

class TestGeoLog:
    def test_geo_log(self):
        list_of_lists_1 = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        result = geo_log(list_of_lists_1)
        expendend = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]

        Generator = geo_log(list_of_lists_1)
        for gen in Generator:
            return gen

        assert list(result) == expendend

class TestIds(TestCase):
    def test_ids(self):
        dict_ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]
       }
        result = [213, 15, 54, 119, 98, 35]
        self.assertEqual(ids(dict_ids), result)

class TestStats(TestCase):
    def test_stats_public(self):
        stats = {'facebook': 55, 'yandex': 120,
                 'vk': 115, 'google': 99,
                 'email': 42, 'ok': 98
        }
        result = 'yandex'
        self.assertEqual(stats_public(stats), result)

class TestYandex(TestCase):
    def test_request_status_get(self):
        self.assertEqual(request_status_get(), 200), "Полученный код состояния не равен ожидаемому"

    def test_request_status_new_folder(self):
        name_path = '1111'
        self.assertEqual(request_status_new_folder(name_path), 201), "Папка с таким именем уже существует"

    def test_passed_create_folder(self):
        self.assertRaises(TypeError, request_status_new_folder('Повторная папка'), 409)




