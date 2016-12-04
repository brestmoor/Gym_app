# -*- coding: utf-8 -*-
import datetime
from collections import OrderedDict
from typing import List


class WeekInfoProvider:
    day_names_pl = [u'Poniedziałek', u'Wtorek', u'Środa', u'Czwartek', u'Piątek', u'Sobota', u'Niedziela']
    day_names_numbers = OrderedDict([('Monday', 0), ('Tuesday', 1), ('Wednesday', 2),
                                     ('Thursday', 3), ('Friday', 4), ('Saturday', 5),
                                     ('Sunday', 6)])

    def __init__(self):
        pass

    def get_current_days_of_the_week(self) -> List[str]:
        now = datetime.datetime.today()
        return self.get_days_of_the_week(now)

    def get_days_of_the_week(self, date: datetime.date) -> List[str]:
        current_day = date.strftime("%A")
        day_number = self.get_curr_day_number(current_day)
        week_days = [self.day_names_pl[day_number]]
        number = day_number + 1
        for i in range(0, 6):
            if number == 7:
                number = 0
            week_days.append(self.day_names_pl[number])
            number += 1

        return week_days

    def get_curr_day_number(self, current_day: str) -> int:
        return self.day_names_numbers[current_day]
