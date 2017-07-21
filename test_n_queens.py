import unittest
import n_queens

class TestNQueens(unittest.TestCase):

    def testFitnessExample(self):
        self.assertEqual(23, n_queens.fitness('32748552'))

    def testFitnessExample2(self):
        self.assertEqual(21, n_queens.fitness('32752124'))

    def testFitnessExample3(self):
        self.assertEqual(22, n_queens.fitness('24752411'))

    def testFitnessExample4(self):
        self.assertEqual(21, n_queens.fitness('32742411'))

    def testFitnessExample5(self):
        self.assertEqual(22, n_queens.fitness('24758552'))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDataSet']
    unittest.main()