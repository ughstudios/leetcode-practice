""" Implementation of Trie data structure """


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_string = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, word: str) -> None:
        """ Insert a string into a Trie Data Structure """
        current = self.root
        for character in word:
            node = current.children.get(character)
            if not node:
                node = TrieNode()
                current.children.update({character: node})
            current = node
        current.end_of_string = True

    def search_string(self, word: str) -> bool:
        current = self.root
        for character in word:
            node = current.children.get(character)
            if not node:
                return False
            current = node
        if current.end_of_string:
            return True
        else:
            return False

    def _delete_str(self, root: TrieNode, word: str, index: int) -> bool:
        char = word[index]
        current = root.children.get(char)

        if len(current.children) > 1:
            self._delete_str(current, word, index + 1)
            return False
        if index == len(word) - 1:
            if len(current.children) >= 1:
                current.end_of_string = False
                return False
            else:
                root.children.pop(char)
                return True

        if current.end_of_string:
            self._delete_str(current, word, index + 1)
            return False

        can_be_deleted = self._delete_str(current, word, index + 1)
        if can_be_deleted:
            root.children.pop(char)
            return True
        else:
            return False

    def delete_str(self, word) -> None:
        self._delete_str(self.root, word, 0)


