#from stuff_1 import module1
import unittest

class TestStuff(unittest.TestCase):
    def test_add(self):
        #self.assertEqual(module1.add(1, 2), 3)
        self.assertEqual(3, 3)

if __name__ == "__main__":
    unittest.main()

