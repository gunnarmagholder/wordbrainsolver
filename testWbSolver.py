import unittest
import wbSolver

class TestWbSolver(unittest.TestCase):
    def setUp(self):
        self.fieldArr = [['d', 'd', 't', 'e', 'z', 'e', 'u'],
                    ['i', 'e', 'g', 'n', 'e', 'r', 'b'],
                    ['e', 'h', 'c', 'u', 'n', 'e', 'v'],
                    ['l', 'u', 'r', 'd', 'u', 't', 'i'],
                    ['t', 'e', 'r', 'e', 'w', 't', 't'],
                    ['i', 'k', 'c', 'g', 't', 'w', 'o'],
                    ['m', 'a', 'l', 'ü', 's', 'ü', 'm'],
                    ]
        self.wordArr = ['mitleid',
                   'motiv',
                   'butter',
                   'wüste',
                   'wunde',
                   'geruch',
                   'zucker',
                   'lüge',
                   'daten']
        self.wb = wbSolver.wbSolver(self.fieldArr, self.wordArr)

    def test_class_init(self):
        self.assertIsInstance(self.wb,wbSolver.wbSolver)

    def test_get_char_at_pos(self):
        self.assertEqual('i',self.wb.getCharAtPos(0,1))

    def test_get_row(self):
        self.assertEqual(['d', 'd', 't', 'e', 'z', 'e', 'u'],self.wb.getRow(0))

if __name__ == '__main__':
    unittest.main()
