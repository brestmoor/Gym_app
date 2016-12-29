# coding=utf-8
from datetime import timedelta, datetime
from typing import Dict, List

from Gym_app.business_logic.schedule import ScheduleProvider
from Gym_app.models.classes_models import PersonalTraining


class PersonalScheduleProvider(ScheduleProvider):
    def get_schedule(self, date: datetime.date) -> Dict[int, List[PersonalTraining]]:
        self.days_dict = self.numerator.numerate(self.weekInfoProvider.get_days_of_the_week(date))
        classes_for_week = list(PersonalTraining.objects.filter(date__range=(date, date + timedelta(days=6))))
        return self._get_filled_schedule(classes_for_week)
