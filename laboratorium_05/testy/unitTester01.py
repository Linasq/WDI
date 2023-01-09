import unittest, random
import test01

class TestWork(unittest.TestCase):
    def test_list_empty(self):
        dane = [(random.randint(0, 99), random.randint(0, 99)) for _ in range(20)]
        result = test01.mordkiSieSzachuja(dane)
        self.assertEqual(result, [])
    def test_S_in_X_cell(self):
        dane=[(random.randint(0, 99), random.randint(0, 99)) for _ in range(100)]
        #dane=[(82, 37), (84, 36), (43, 39), (45, 38), (31, 79), (29, 78), (10,10), (12,11)]
        result=test01.mordkiSieSzachuja(dane)
        tab=[]
        for i in result:
            for x,y in i:
              tab.append((x,y))
        #self.assertIn((82, 37), tab)
        self.assertIn((10,10), tab)


if __name__=='__main__':
    unittest.main()