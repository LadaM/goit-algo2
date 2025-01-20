from trie import Trie


class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(word, str) for word in strings):
            raise TypeError("Input must be a list of strings.")

        if not strings:
            return ""

        for word in strings:
            self.put(word)

        current = self.root
        common_prefix = []

        while True:
            if len(current.children) == 1 and current.value is None:
                char = next(iter(current.children))  # Get the single child character
                common_prefix.append(char)
                current = current.children[char]
            else:
                break

        return "".join(common_prefix)


if __name__ == "__main__":
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = []
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["a"]
    assert trie.find_longest_common_word(strings) == "a"

    print("All tests passed.")
