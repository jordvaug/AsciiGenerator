import unittest
from cache import Cache


class TestCache(unittest.TestCase):


    def test_load_cache(self):
        cache = Cache(10)
        self.assertEqual(len(cache.cache), 1)

    def test_get(self):
        cache = Cache(10)
        value = cache.get("c22bfafbdd525c696b94f87b72d0ac1e287b5f22ee9091cb2e3781b5fa0b113e")
        self.assertEqual(len(value), 72)

if __name__ == "__main__":
    unittest.main()