# coding=utf-8
from collections import OrderedDict
from datetime import timedelta, datetime, time
from typing import Dict, List

from Gym_app.business_logic.schedule import Numerator
from Gym_app.business_logic.schedule.week_info_provider import WeekInfoProvider
from Gym_app.models import Class


class ScheduleProvider:
    def __init__(self):
        self.days_dict = OrderedDict()
        self.weekInfoProvider = WeekInfoProvider()
        self.numerator = Numerator()

    def get_current_schedule(self):
        return self.get_schedule(datetime.today())

    def get_schedule(self, date: datetime.date) -> Dict[int, List[Class]]:
        self.days_dict = self.numerator.numerate(self.weekInfoProvider.get_days_of_the_week(date))
        classes_for_week = list(Class.objects.filter(date__range=(date, date + timedelta(days=6))))
        return self.__get_filled_schedule(classes_for_week)

    def __get_filled_schedule(self, classes_for_week: List[Class]) -> Dict[int, List[Class]]:
        schedule = OrderedDict()
        for hour in range(9, 20):
            self.__add_blank_row(hour, schedule)
            classes_for_hour = self.__filter_classes_for_hour(classes_for_week, hour)
            self.__place_classes(hour, classes_for_hour, schedule)

        return schedule

    def __filter_classes_for_hour(self, classes_for_week, hour):
        return [c for c in classes_for_week if
                c.class_in_schedule is not None and c.class_in_schedule.start_time == time(hour, 0)]

    def __place_classes(self, hour, classes_for_hour, schedule):
        for single_class in classes_for_hour:
            schedule[hour][self.days_dict[single_class.class_in_schedule.day]] = single_class

    def __add_blank_row(self, hour, schedule):
        row = [None, None, None, None, None, None, None]
        schedule[hour] = row
