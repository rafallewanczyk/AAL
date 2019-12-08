import unittest
from algorithms.HashTable import HashTable

class MyTestCase(unittest.TestCase):

    def test_size(self):
        hashtable = HashTable(200)
        hashtable.insert("test1")
        hashtable.insert("test2")
        hashtable.insert("test3")
        hashtable.delete("test1")
        self.assertEqual(hashtable.getSize(), 2)

    def test_insert(self):
        hashtable = HashTable(200)
        hashtable.insert("test")
        self.assertEqual("test" in hashtable.array, True)

    def test_delete(self):
        hashtable= HashTable(200)
        hashtable.insert("test")
        hashtable.delete("test")
        self.assertEqual("test" not in hashtable.array, True)

    def test_cant_find(self):
        hashtable = HashTable(200)
        self.assertEqual(hashtable.find("test"), -1)

    def test_getHashValue(self):
        hashtable = HashTable(200)
        # "Ścieżka = (97 * 380^0 + 107 * 380^1 + 380 * 380^2 + 101  * 380^3 + 105 * 380^4 + 99 * 380^5 + 346 * 380^6) MOD 200 = 157
        self.assertEqual(hashtable.getHashValue("Ścieżka"),157)

    def test_powerMod(self):
        self.assertEqual(HashTable(200).powerMod(1243, 456, 200), 1 )

    def test_find(self):
        hashtable = HashTable(200)
        hashtable.insert("Ścieżka")
        self.assertEqual(hashtable.find("Ścieżka"), 157)

    def test_collision(self):
        hashtable = HashTable(200)
        hashtable.array[157] = "zajete"
        hashtable.array[158] = "zajete"
        hashtable.insert("Ścieżka")
        self.assertEqual(hashtable.find("Ścieżka"), 161)

    def test_find_after_collision_and_deletetion(self):
        hashtable = HashTable(3)
        #hashvalue(test) = hashvalue(rafal) = 1
        hashtable.insert("test")
        hashtable.insert("rafal")
        hashtable.delete("test")
        self.assertEqual(hashtable.find("rafal"), 2)


if __name__ == '__main__':
    unittest.main()
