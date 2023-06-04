""" Tests the implementation of the Trie data structure """
from trie import Trie


def test_trie() -> None:
    trie = Trie()
    trie.insert_string("App")
    trie.insert_string("Appl")
    assert trie.search_string('App')
    assert trie.search_string('Appl')
    trie.delete_str('App')
    assert not trie.search_string('App')
