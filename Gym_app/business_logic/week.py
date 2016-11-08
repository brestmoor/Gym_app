# -*- coding: utf-8 -*-
import datetime
from collections import OrderedDict


class WeekInfoProvider:
    day_names_pl = [u'Poniedziałek', u'Wtorek', u'Środa', u'Czwartek', u'Piątek', u'Sobota', u'Niedziela']
    day_names_numbers = OrderedDict([('Monday', 0), ('Tuesday', 1), ('Wednesday', 2),
                                     ('Thursday', 3), ('Friday', 4), ('Saturday', 5),
                                     ('Sunday', 6)])

    def __init__(self):
        pass

    def get_current_week_days(self):
        now = datetime.datetime.now()
        current_day = now.strftime("%A")
        curr_day_number = self.get_curr_day_number(current_day)
        return self.get_week_days(curr_day_number)

    def get_curr_day_number(self, current_day):
        return self.day_names_numbers[current_day]

    def get_week_days(self, current_day_number):
        week_days = [self.day_names_pl[current_day_number]]
        number = current_day_number + 1
        for i in xrange (0,6):
            if number == 7:
                number = 0
            week_days.append(self.day_names_pl[number])
            number += 1

        return week_days

