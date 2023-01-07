import unittest, random
import toTest

class TestWork(unittest.TestCase):
    def test_list_int(self):
        dane = [(random.randint(0, 99), random.randint(0, 99)) for _ in range(10)]
        result = toTest.mordkiSieSzachuja(dane)
        self.assertEqual(result, [])
        #self.assertTrue(result==[])

if __name__=='__main__':
    unittest.main()