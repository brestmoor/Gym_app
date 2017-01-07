import collections
from collections import OrderedDict
from collections import defaultdict

from Gym_app.business_logic.schedule import WeekInfoProvider


class Grouper:
    def group(self, exercises):
        result = defaultdict(lambda: [None, None, None, None, None, None, None])
        days_of_the_week = WeekInfoProvider.day_names_numbers_pl
        for exercise in exercises:
            result[exercise.order][days_of_the_week[exercise.day]] = exercise

        return result

