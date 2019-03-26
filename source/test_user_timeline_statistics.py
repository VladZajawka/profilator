from unittest import TestCase
import json
from user_timeline_statistics import UserTimelineStatistics
from twitter import Status


class TestUserTimelineStatistics(TestCase):

    @classmethod
    def setUpClass(cls):
        with open("sample_test_data.json", "r") as file:
            timeline = json.load(file)
            cls.timeline = [Status.NewFromJsonDict(status) for status in timeline]
        cls.stats = UserTimelineStatistics()

    def test_replies_count(self):
        # sprawdza działanie w/w metody w przypadku podania poprawych danych i zbioru pustego
        self.assertEqual(self.stats.replies_count(self.timeline), 8)
        self.assertEqual(self.stats.replies_count([]), 0)

    def test_replies_count_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.replies_count, 43)
        self.assertRaises(TypeError, self.stats.replies_count, True)
        self.assertRaises(TypeError, self.stats.replies_count, "ananas")
        self.assertRaises(TypeError, self.stats.replies_count, [21, False, "szpinak"])

    def test_replies_percentage(self):
        # sprawdza działanie w/w metody w przypadku podania poprawych danych i zbioru pustego
        self.assertAlmostEqual(self.stats.replies_percentage(self.timeline), 8/20*100)
        self.assertRaises(ValueError, self.stats.replies_percentage, [])

    def test_replies_percentage_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.replies_percentage, 23)
        self.assertRaises(TypeError, self.stats.replies_percentage, False)
        self.assertRaises(TypeError, self.stats.replies_percentage, "rzepa")
        self.assertRaises(TypeError, self.stats.replies_percentage, [True, 39, "marchew"])

    def test_day_counter(self):
        # sprawdza działanie w/w metody w przypadku podania poprawych danych i zbioru pustego
        self.assertEqual(self.stats.day_counter(self.timeline), {'Thu': 3, 'Wed': 3, 'Sat': 2, 'Sun': 1, 'Tue': 1})
        self.assertEqual(self.stats.day_counter([]), TypeError)

    def test_average_favourites(self):
        # sprawdza działanie w/w metody w przypadku podania prawidłowych danych i zbioru pustego
        self.assertAlmostEqual(self.stats.average_favourites(self.timeline), 20/39)
        self.assertEqual(self.stats.average_favourites([]), 0)

    def test_average_favourites_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        with open("test_average_favorites.json", "r") as file:
            favourites_with_error = json.load(file)
            favourites_with_error = [Status.NewFromJsonDict(status) for status in favourites_with_error]

        self.assertRaises(TypeError, self.stats.average_favourites, favourites_with_error)
        
    def test_hours_count_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.replies_count, 43)
        self.assertRaises(TypeError, self.stats.replies_count, True)
        self.assertRaises(TypeError, self.stats.replies_count, "ananas")
        self.assertRaises(TypeError, self.stats.replies_count, [21, False, "szpinak"])
        
    def test_avg_hour_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.replies_count, 43)
        self.assertRaises(TypeError, self.stats.replies_count, True)
        self.assertRaises(TypeError, self.stats.replies_count, "ananas")
        self.assertRaises(TypeError, self.stats.replies_count, [21, False, "szpinak"])
        
    def test_KMeans_clusters_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.replies_count, 43)
        self.assertRaises(TypeError, self.stats.replies_count, True)
        self.assertRaises(TypeError, self.stats.replies_count, "ananas")
        self.assertRaises(TypeError, self.stats.replies_count, [21, False, "szpinak"])

    def test_day_counter(self):
        # sprawdza działanie w/w metody w przypadku podania poprawych danych
        self.assertEqual(self.stats.day_counter(self.timeline), {'Tue': 20})

    def test_day_counter_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.day_counter, 43)
        self.assertRaises(TypeError, self.stats.day_counter, True)
        self.assertRaises(TypeError, self.stats.day_counter, "ananas")
        self.assertRaises(TypeError, self.stats.day_counter, [21, False, "szpinak"])

    def test_most_active_day(self):
        # sprawdza działanie w/w metody w przypadku podania poprawych danych
        self.assertEqual(self.stats.most_active_day(self.timeline), 'Tue')

    def test_most_active_day_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.most_active_day, 43)
        self.assertRaises(TypeError, self.stats.most_active_day, True)
        self.assertRaises(TypeError, self.stats.most_active_day, "ananas")
        self.assertRaises(TypeError, self.stats.most_active_day, [21, False, "szpinak"])

    def test_KMeans_day_clusters(self):
        # sprawdza działanie w/w metody w przypadku podania poprawych danych
        self.assertEqual(self.stats.most_active_day(self.timeline), 'Tue')

    def test_KMeans_day_clusters_with_errors(self):
        # sprawdza działanie w/w metody w przypadku podania błędnych danych
        self.assertRaises(TypeError, self.stats.most_active_day, 43)
        self.assertRaises(TypeError, self.stats.most_active_day, True)
        self.assertRaises(TypeError, self.stats.most_active_day, "ananas")
        self.assertRaises(TypeError, self.stats.most_active_day, [21, False, "szpinak"])
