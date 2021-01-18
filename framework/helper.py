from random import randint


def generate_random_id(start: int = 1, end: int = 100):
    """Генерация случайного id от 1 до 100 по умолчанию"""
    return randint(start, end)


def generate_json_data(user_id: int = generate_random_id(end=10),
                       title: str = 'foo',
                       body: str = 'bar'):
    return {'userId': user_id,
            'title': title,
            'body': body}
