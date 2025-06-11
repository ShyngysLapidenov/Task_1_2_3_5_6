#Task 3
import requests
import logging
from collections import Counter, defaultdict
import re

logging.basicConfig(
    filename='api_script.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def fetch_data():
    url = 'https://jsonplaceholder.typicode.com/posts'
    logging.info(f'Запрос к API: {url}')
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info('Успешно получены данные от API')
        return response.json()
    except requests.RequestException as e:
        logging.error(f'Ошибка при получении данных: {e}')
        return []

def analyze_data(posts):
    logging.info('Анализ данных')

    user_ids = [post['userId'] for post in posts]
    user_post_counts = Counter(user_ids)

    titles = [post['title'] for post in posts]
    bodies = [post['body'] for post in posts]

    avg_title_length = sum(len(t) for t in titles) / len(titles)
    avg_body_length = sum(len(b) for b in bodies) / len(bodies)

    title_words = Counter(re.findall(r'\w+', ' '.join(titles).lower()))
    body_words = Counter(re.findall(r'\w+', ' '.join(bodies).lower()))

    top_title_words = title_words.most_common(5)
    top_body_words = body_words.most_common(5)

    # Анализ типов данных по ключам
    type_counter = defaultdict(Counter)
    for post in posts:
        for key, value in post.items():
            type_name = type(value).__name__
            type_counter[key][type_name] += 1

    return {
        'user_post_counts': user_post_counts,
        'avg_title_length': avg_title_length,
        'avg_body_length': avg_body_length,
        'top_title_words': top_title_words,
        'top_body_words': top_body_words,
        'field_types': type_counter
    }

def save_results(analysis):
    logging.info('Сохранение результатов в result.txt')
    with open('result.txt', 'w', encoding='utf-8') as f:
        f.write('Анализ данных из JSONPlaceholder:\n\n')

        f.write('Количество постов по пользователям:\n')
        for user_id, count in analysis['user_post_counts'].items():
            f.write(f'Пользователь {user_id}: {count} постов\n')

        f.write('\nСредняя длина заголовков: {:.2f} символов\n'.format(analysis['avg_title_length']))
        f.write('Средняя длина тел постов: {:.2f} символов\n'.format(analysis['avg_body_length']))

        f.write('\nТоп-5 слов в заголовках:\n')
        for word, count in analysis['top_title_words']:
            f.write(f'"{word}": {count} раз(а)\n')

        f.write('\nТоп-5 слов в телах постов:\n')
        for word, count in analysis['top_body_words']:
            f.write(f'"{word}": {count} раз(а)\n')

        f.write('\nТипы данных по каждому полю:\n')
        for field, types in analysis['field_types'].items():
            f.write(f'Поле "{field}":\n')
            for t, count in types.items():
                f.write(f'  {t}: {count} раз(а)\n')

def main():
    logging.info('Скрипт запущен')
    data = fetch_data()
    if data:
        analysis = analyze_data(data)
        save_results(analysis)
        logging.info('Скрипт завершён успешно')
    else:
        logging.warning('Скрипт завершён без результатов')

if __name__ == '__main__':
    main()
