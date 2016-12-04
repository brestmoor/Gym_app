from unittest import TestCase

from Gym_app.business_logic.schedule import Numerator


class DaysNumeratorTest(TestCase):
    def test_should_numerate(self):
        # given
        days = ["Ala", "ma", "kota"]
        # when
        result = Numerator().numerate(days)
        # then
        self.assertEqual(result, {"Ala": 0, "ma": 1, "kota": 2})
