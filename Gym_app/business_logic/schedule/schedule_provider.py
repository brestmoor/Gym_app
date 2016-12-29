# coding=utf-8
from abc import ABCMeta, abstractmethod
from collections import OrderedDict
from datetime import timedelta, datetime, time
from typing import Dict, List

from Gym_app.business_logic.schedule import Numerator
from Gym_app.business_logic.schedule.week_info_provider import WeekInfoProvider
from Gym_app.models import GroupClass


class ScheduleProvider(metaclass=ABCMeta):
    def __init__(self):
        self.days_dict = OrderedDict()
        self.weekInfoProvider = WeekInfoProvider()
        self.numerator = Numerator()

    def get_current_schedule(self):
        return self.get_schedule(datetime.today())

    @abstractmethod
    def get_schedule(self, date: datetime.date) -> Dict[int, List[GroupClass]]:
        pass

    def _get_filled_schedule(self, classes_for_week: List[GroupClass]) -> Dict[int, List[GroupClass]]:
        schedule = OrderedDict()
        for hour in range(9, 20):
            self._add_blank_row(hour, schedule)
            classes_for_hour = self._filter_classes_for_hour(classes_for_week, hour)
            self._place_classes(hour, classes_for_hour, schedule)

        return schedule

    def _filter_classes_for_hour(self, classes_for_week, hour):
        return [c for c in classes_for_week if
                c.class_in_schedule is not None and c.class_in_schedule.start_time == time(hour, 0)]

    def _place_classes(self, hour, classes_for_hour, schedule):
        for single_class in classes_for_hour:
            schedule[hour][self.days_dict[single_class.class_in_schedule.day]] = single_class

    def _add_blank_row(self, hour, schedule):
        row = [None, None, None, None, None, None, None]
        schedule[hour] = row
