# -*- coding: utf-8 -*-
from unittest import TestCase

# Create your tests here.
from Gym_app.business_logic.week import WeekInfoProvider


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
        days_names_from_monday = week_info_provider.get_week_days(0)
        days_names_from_tuesday = week_info_provider.get_week_days(1)
        days_names_from_wednesday = week_info_provider.get_week_days(2)
        days_names_from_thursday = week_info_provider.get_week_days(3)
        days_names_from_friday = week_info_provider.get_week_days(4)
        days_names_from_saturday = week_info_provider.get_week_days(5)
        days_names_from_sunday = week_info_provider.get_week_days(6)
        
        # then
        self.assertEqual(days_names_from_monday , ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"])
        self.assertEqual(days_names_from_tuesday , ["Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela", "Poniedziałek"])
        self.assertEqual(days_names_from_wednesday , ["Środa", "Czwartek", "Piątek", "Sobota", "Niedziela", "Poniedziałek", "Wtorek"])
        self.assertEqual(days_names_from_thursday , ["Czwartek", "Piątek", "Sobota", "Niedziela", "Poniedziałek", "Wtorek", "Środa"])
        self.assertEqual(days_names_from_friday , ["Piątek", "Sobota", "Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek"])
        self.assertEqual(days_names_from_saturday , ["Sobota", "Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"])
        self.assertEqual(days_names_from_sunday , ["Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota"])

        print days_names_from_wednesday