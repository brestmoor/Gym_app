# -*- coding: utf-8 -*-
import datetime
from unittest import TestCase

from Gym_app.business_logic.schedule.week_info_provider import WeekInfoProvider


class WeekInfoTest(TestCase):
    def test_correct_day_number_is_returned(self):
        # given
        week_info_provider = WeekInfoProvider()

        # when
        curr_day_number = week_info_provider.get_curr_day_number('Monday')
        curr_day_number5 = week_info_provider.get_curr_day_number('Saturday')

        # then
        self.assertEqual(curr_day_number, 0)
        self.assertEqual(curr_day_number5, 5)

    def test_correct_week_days_are_returned(self):
        # given
        week_info_provider = WeekInfoProvider()

        # when
        days_names_from_monday = week_info_provider.get_days_of_the_week(datetime.date(2016, 11, 21))
        days_names_from_tuesday = week_info_provider.get_days_of_the_week(datetime.date(2016, 11, 22))
        days_names_from_wednesday = week_info_provider.get_days_of_the_week(datetime.date(2016, 11, 23))
        days_names_from_thursday = week_info_provider.get_days_of_the_week(datetime.date(2016, 11, 24))
        days_names_from_friday = week_info_provider.get_days_of_the_week(datetime.date(2016, 11, 25))
        days_names_from_saturday = week_info_provider.get_days_of_the_week(datetime.date(2016, 11, 26))
        days_names_from_sunday = week_info_provider.get_days_of_the_week(datetime.date(2016, 11, 27))

        # then
        self.assertEqual(days_names_from_monday,
                         ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"])
        self.assertEqual(days_names_from_tuesday,
                         ["Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela", "Poniedziałek"])
        self.assertEqual(days_names_from_wednesday,
                         ["Środa", "Czwartek", "Piątek", "Sobota", "Niedziela", "Poniedziałek", "Wtorek"])
        self.assertEqual(days_names_from_thursday,
                         ["Czwartek", "Piątek", "Sobota", "Niedziela", "Poniedziałek", "Wtorek", "Środa"])
        self.assertEqual(days_names_from_friday,
                         ["Piątek", "Sobota", "Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek"])
        self.assertEqual(days_names_from_saturday,
                         ["Sobota", "Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"])
        self.assertEqual(days_names_from_sunday,
                         ["Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota"])

        print(days_names_from_wednesday)
