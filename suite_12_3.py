import unittest
import test_12_3


toster = unittest.TestSuite()
toster.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
toster.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
runner_of_test = unittest.TextTestRunner(verbosity=2)
runner_of_test.run(toster)
