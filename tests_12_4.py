import logging
import unittest
import rt_with_exceptions


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner1 = rt_with_exceptions.Runner("Oleg", -5)
            for _ in range(10):
                runner1.walk()
            self.assertEqual(runner1.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner1 = rt_with_exceptions.Runner(["Oleg", 228])
            for _ in range(10):
                runner1.run()
            self.assertEqual(runner1.distance, 100)
            logging.info('test_walk" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = rt_with_exceptions.Runner("Oleg")
        runner2 = rt_with_exceptions.Runner("Ne Oleg")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
