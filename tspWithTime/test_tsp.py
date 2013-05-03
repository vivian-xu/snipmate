import unittest
import tsp


class test_tsp(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_isOverWeight(self):
        choices = {(3, 6): True, (1, 2, 4): False, (): False}
        for choice, expt in choices.items():
            res = tsp.isOverWeight(choice)
            self.assertEquals(res, expt)

    def test_single_car(self):
        clients = [2, 3, 4]
        self.assertEquals(tsp.single_car(clients),
                          [[2], [3], [3, 2], [4], [4, 2], [4, 3]])

    def test_list2set(self):
        testdata = [[2, 4], [2, 5, 6, 7], [[9, 8, 7]]]
        self.assertEquals(tsp.list2set(testdata), {2, 4, 5, 6, 7, 8, 9})
        self.assertEquals(tsp.list2set([[1, 2], [2, 4]]), {1, 2, 4})
        self.assertEquals(tsp.list2set([1, 2, 5]), {1, 2, 5})

    def test_isTimeOk(self):
        #self.assertEquals(tsp.isTimeOk(0, 1)
        print(tsp.isTimeOk(0, 1))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(test_tsp('test_isOverWeight'))
    suite.addTest(test_tsp('test_single_car'))
    suite.addTest(test_tsp('test_list2set'))
    suite.addTest(test_tsp('test_isTimeOk'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
