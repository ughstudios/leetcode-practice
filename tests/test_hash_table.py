""" Tests for hash table implementation """
from hashing import HashTable


def test_hash_table() -> None:
    table = HashTable()
    table.put('test', 1)
    assert table.get('test') == 1

    table['test'] = 5
    assert table['test'] == 5

    test_array = ['pizza']
    table['testerino'] = test_array
    assert  table['testerino'] == test_array


