from trie import Trie


class Homework(Trie):
    def has_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument for has_prefix: prefix = {prefix} must be a string"
            )

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        # if traversal completed successfully, the prefix exists
        return True

    def count_words_with_suffix(self, suffix):
        if not isinstance(suffix, str):
            raise TypeError(
                f"Illegal argument for countWordsWithSuffix: suffix = {suffix} must be a string"
            )

        def traverse_and_count(node, current_word):
            count = 0

            if node.value is not None:
                if current_word.endswith(suffix):
                    count += 1

            for char, child in node.children.items():
                count += traverse_and_count(child, current_word + char)

            return count

        return traverse_and_count(self.root, "")


if __name__ == "__main__":
    trie = Homework()
    words = ["banana", "bandana", "band", "bandage", "banner", "apple", "application", "cat"]
    for index, word in enumerate(words):
        trie.put(word, index)

    print(trie.has_prefix("app"))  # True ("apple", "application")
    print(trie.has_prefix("ban"))  # True ("banana", "bandana", "band", "bandage", "banner")
    print(trie.has_prefix("cat"))  # True ("cat")
    print(trie.has_prefix("dog"))  # False

    print(trie.count_words_with_suffix("ana"))  # 2 ("banana", "bandana")
    print(trie.count_words_with_suffix("band"))  # 1 ("band")
    print(trie.count_words_with_suffix("cat"))  # 1 ("cat")
    print(trie.count_words_with_suffix("dog"))  # 0
