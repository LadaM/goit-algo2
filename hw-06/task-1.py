import string
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import requests


def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return None


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def map_function(word):
    return word, 1


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()


def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)


def map_reduce(text, search_words=None):
    text = remove_punctuation(text)
    words = text.split()

    if search_words:
        words = [word for word in words if word in search_words]

    # 1 - map (parallel)
    with ThreadPoolExecutor() as executor:
        mapped_values = list(executor.map(map_function, words))

    # 2 - shuffle
    shuffled_values = shuffle_function(mapped_values)

    # 3 - reduce (parallel)
    with ThreadPoolExecutor() as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))

    return dict(reduced_values)


if __name__ == "__main__":
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    text = get_text(url)
    if text:
        search_words = ["war", "peace", "love"]
        result = map_reduce(text, search_words)

        print("Результат підрахунку слів:", result)
    else:
        print("Помилка: Не вдалося отримати вхідний текст.")
