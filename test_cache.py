import unittest
from cache import Cache


class TestCache(unittest.TestCase):


    def test_load_cache(self):
        cache = Cache(10)
        self.assertEqual(len(cache.cache), 1)

    def test_get(self):
        cache = Cache(10)
        cache.get("gc.jpg")
        self.assertEqual(len(cache.cache), 1)

if __name__ == "__main__":
    unittest.main()