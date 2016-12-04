import django

django.setup()

from .days_numerator import Numerator
from .schedule_provider import ScheduleProvider
from .week_info_provider import WeekInfoProvider
