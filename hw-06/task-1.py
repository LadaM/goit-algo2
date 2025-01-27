import string
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import requests
import matplotlib.pyplot as plt


def get_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException:
        return None


def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


def map_function(word):
    return word.lower(), 1


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


def visualize_top_words(word_counts, top_n=10):
    # sort by frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*sorted_words)

    # make plot
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts)
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.title(f"Top-{top_n} words")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"

    text = get_text(url)
    if text:
        word_counts = map_reduce(text)
        visualize_top_words(word_counts, top_n=20)
    else:
        print("Error fetching text.")
