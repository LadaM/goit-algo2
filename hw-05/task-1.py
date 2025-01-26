import mmh3
from bitarray import bitarray


class BloomFilter:
    def __init__(self, size, num_hashes):
        """
        :param size: size of the bit array.
        :param num_hashes: number of hash functions.
        """
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def _hashes(self, item):
        """
        Generates hashes for the given item.

        :param item: element to hash.
        :return: hash generator.
        """
        for i in range(self.num_hashes):
            yield mmh3.hash(item, i) % self.size

    def add(self, item):
        """
        Add an item to the filter.

        :param item: element to be added.
        """
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def contains(self, item):
        """
        Перевірка, чи є елемент у фільтрі.

        :param item: Елемент для перевірки.
        :return: True, якщо елемент може бути у фільтрі, інакше False.
        """
        for i in self._hashes(item):
            if self.bit_array[i] == 0:
                return False

        return True


def check_password_uniqueness(bloom_filter, passwords):
    """
    Checking password uniqueness with BloomFilter

    :param bloom_filter: BloomFilter instance.
    :param passwords: list of passwords to check.
    :return: dictionary with results.
    """
    results = {}
    for password in passwords:
        if not isinstance(password, str) or not password.strip():
            results[password] = "Некоректний пароль"
            continue

        if bloom_filter.contains(password):
            results[password] = "Використовувався раніше"
        else:
            results[password] = "Новий пароль"
            bloom_filter.add(password)

    return results


if __name__ == "__main__":
    # Ініціалізація фільтра Блума
    bloom = BloomFilter(size=1000, num_hashes=3)

    # Додавання існуючих паролів
    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    # Перевірка нових паролів
    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest", ""]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    # Виведення результатів
    for password, status in results.items():
        print(f"Пароль '{password}' - {status}.")
