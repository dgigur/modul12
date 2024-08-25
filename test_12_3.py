import runner, runner_and_tournament
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = runner.Runner("Oleg")
        for _ in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner1 = runner.Runner("Oleg")
        for _ in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = runner.Runner("Oleg")
        runner2 = runner.Runner("Ne Oleg")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    k = 1
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner_2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner_3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(key, ":", value)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def place_calc(self, arg):
        places = arg.start()  # Словарь: ключ - позиция, значение - объект класса runner
        udapted_places = {x: y.name for x, y in places.items()}
        # Добавляем в общий список тестов результат с отображением мест и имен. Так понятнее, что получилось.
        # Можно в общий список добавлять с отображением мест и объектов класса runner, тогда udapted_places -> places
        self.all_results.update({f"test {TournamentTest.k}": udapted_places})
        self.assertTrue(udapted_places[max(udapted_places.keys())] == "Ник")
        for i in range(1, len(places)):
            self.assertLess(list(places.values())[i].speed, list(places.values())[i - 1].speed)
        TournamentTest.k += 1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        tour_1 = runner_and_tournament.Tournament(3, self.runner_1, self.runner_3)
        self.place_calc(tour_1)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        tour_2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.place_calc(tour_2)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        tour_3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.place_calc(tour_3)