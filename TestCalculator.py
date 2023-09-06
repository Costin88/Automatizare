# from Calculator import Calculator

# def test_Calculator():
#     calc = Calculator()
#     result = calc.sumFromNumbers(2,3)
#     if result == 5:
#         print("Test passed")
#     else:
#         print("Test failed")
    

# test_Calculator()    

#unittest
# import unittest
# from Calculator import Calculator
 
# class testSumFromNumbers(unittest.TestCase):
#     def test_sumFromNumbers(self):
#         calc = Calculator()
#         result = calc.sumFromNumbers(2,3)
#         expected = 5
#         self.assertEqual(result,expected)
#         self.assertNotEqual(result,expected) 
#         self.assertGreaterEqual(result,expected)
        # se poate inlocui structura if cu assertEqual
        # if result == 5:
        #     print("Test passed")
        # else:
        #     print("Test failed")
        
# unittest.main()
# Crearea unui grup de teste
import unittest
from Calculator import Calculator
 
class testSumFromNumbers(unittest.TestCase):
    def test_isCorect(self):
        calc = Calculator()
        result = calc.sumFromNumbers(2,3)
        expected = 5
        self.assertEqual(result,expected)
 
 
    def test_isNegative(self):
        calc = Calculator()
        result = calc.sumFromNumbers(-4,1)
        expected = 0
        self.assertLess(result,expected)
 
 
    def test_isGreater(self):
        calc = Calculator()
        result = calc.sumFromNumbers(2,3)
        expected = 5
        self.assertGreaterEqual(result,expected)
 
def suite():
    # gather all tests in a test suite
 
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testSumFromNumbers))
 
    return test_suite
 
mySuite=suite()
 
#define Runner
 
runner=unittest.TextTestRunner()
runner.run(mySuite)