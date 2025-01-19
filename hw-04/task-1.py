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


if __name__ == "__main__":
    trie = Homework()
    words = ["banana", "bandana", "band", "bandage", "banner", "bat", "source", "cat"]
    for word in words:
        trie.put(word)

    print(trie.has_prefix("app"))  # True ("apple", "application")
    print(trie.has_prefix("ban"))  # True ("banana", "bandana", "band", "bandage", "banner")
    print(trie.has_prefix("cat"))  # True ("cat")
    print(trie.has_prefix("dog"))  # False
