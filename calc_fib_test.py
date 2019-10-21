import unittest
import calc_fib
import time


class TestFibFunc(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%s: %.3f" % (self.id(), t))

    def test_recurssivefib(self):
        time.sleep(1)
        self.assertEqual(calc_fib.recurssive_fib(40), 102334155)

    def test_fib(self):
        time.sleep(2)
        self.assertEqual(calc_fib.fib(40), 102334155)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFibFunc)
    unittest.TextTestRunner(verbosity=0).run(suite)
