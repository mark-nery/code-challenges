import small_problem
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.input = small_problem.SmallProblem("2\n100\n3\n5 75 25\n100\n4\n15 5 50 50")
        self.null_input = small_problem.SmallProblem("")
        self.nonsense =  small_problem.SmallProblem("asldfjasl")

    def test_parse_string(self):
        self.assertEqual(self.input.get_input_array() , ['2', '100', '3', '5 75 25', '100', '4', '15 5 50 50'])

    def test_get_cases(self):
        self.assertEqual(self.input.get_cases(),2)
        self.assertEqual(self.null_input.get_cases(),0)
        self.assertEqual(self.nonsense.get_cases(),0)

    def test_get_credits(self):
        self.assertEqual(self.input.get_credits(),[100,100])
        self.assertEqual(len(self.input.get_credits()),self.input.get_cases())
        self.assertEqual(self.null_input.get_credits(),[])
        self.assertEqual(self.nonsense.get_credits(),[])

    def test_get_prices(self):
        self.assertEqual(self.input.get_prices(),[[5,75,25],[15,5,50,50]])
        self.assertEqual(self.null_input.get_credits(),[])
        self.assertEqual(self.nonsense.get_credits(),[])

    
    def test_find_indexes(self):
        arr = [15 ,5, 50, 50]
        self.assertEqual(self.input.find_indexes(arr,50),[3,4])
        
    def test_select_items(self):
        self.assertEqual(self.input.select_items()[0],[2,3])
        self.assertEqual(self.input.select_items()[1],[3,4])

    
    def test_print_results(self):
        self.assertEqual(self.input.print_results(),"Case #1: 2 3\nCase #2: 3 4\n")

        
if __name__ == '__main__':
    unittest.main()
