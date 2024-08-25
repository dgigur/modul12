import runner_and_tournament
import unittest


# Ошибка в логике в том, что если дистанция меньше скорости самого медленного и самый медленный записан в списке
# участников первым, то он за 1 итерацию пройдет всю дистанцию и окажется первым. В целом если дистанция меньше, чем
# скорость минимум двух участников, то места между участниками, чья скорость больше дистанции, будут распределяться
# в зависимости от их порядка в очереди. Решение внизу.


class TournamentTest(unittest.TestCase):
    k = 1

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner_and_tournament.Runner("Усэйн", 10)
        self.runner_2 = runner_and_tournament.Runner("Андрей", 9)
        self.runner_3 = runner_and_tournament.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(key, ":", value)

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

    def test_run_1(self):
        tour_1 = runner_and_tournament.Tournament(3, self.runner_1, self.runner_3)
        self.place_calc(tour_1)

    def test_run_2(self):
        tour_2 = runner_and_tournament.Tournament(90, self.runner_2, self.runner_3)
        self.place_calc(tour_2)

    def test_run_3(self):
        tour_3 = runner_and_tournament.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.place_calc(tour_3)

# Одним из способов решения может выступить формирование списка участников по порядку от самого быстрого
# к самому медленному, а затем вести расчет по порядку этого списка. Для этого в методе start перед циклом вводим
# self.participants.sort(key=lambda x: x.speed, reverse=True) а в тестах сравниваем что скорость каждого следующего
# участника меньше чем у предыдущего
