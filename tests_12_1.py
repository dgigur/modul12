import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = runner.Runner("Oleg")
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner1 = runner.Runner("Oleg")
        for _ in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)
    def test_challenge(self):
        runner1 = runner.Runner("Oleg")
        runner2 = runner.Runner("Ne Oleg")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)\

