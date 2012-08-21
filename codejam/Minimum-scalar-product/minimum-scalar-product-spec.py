from minimum_scalar_product import *
import unittest

class TestSequenceFunctions(unittest.TestCase):
   
    def test_scalar(self):
        self.assertEqual(scalar([1,2,3],[3,2,1]) ,10 )

    def test_min_scalar_permutation(self):
        self.assertEqual(min_scalar_permutations([1,2],[3,4]),10)

    def test_sample_data(self):
        self.assertEqual(min_scalar_permutations([1,3,-5],[-2,4,1]),-25)
        self.assertEqual(min_scalar_permutations([1,2,3,4,5],[1,0,1,0,1]),6)

    def test_trials(self):
        self.assertEqual(trials("2\nlfkasdjflasl;sldf"),2)

    def test_vectors(self):
        self.assertEqual(vectors("2\n3\n1 2 3\n3 4 5"),[[1,2,3],[3,4,5]])
if __name__ == '__main__':
    unittest.main()
