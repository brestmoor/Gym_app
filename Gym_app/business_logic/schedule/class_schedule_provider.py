# coding=utf-8
from datetime import timedelta, datetime
from typing import Dict, List

from Gym_app.business_logic.schedule import ScheduleProvider
from Gym_app.models import GroupClass


class GroupClassScheduleProvider(ScheduleProvider):
    def get_schedule(self, date: datetime.date) -> Dict[int, List[GroupClass]]:
        self.days_dict = self.numerator.numerate(self.weekInfoProvider.get_days_of_the_week(date))
        classes_for_week = list(GroupClass.objects.filter(date__range=(date, date + timedelta(days=6))))
        return self._get_filled_schedule(classes_for_week)
