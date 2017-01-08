from typing import List

from Gym_app.models import Goal
from Gym_app.models import GoalRecord
from Gym_app.models import PartialGoal


class AchievementsConverter:
    def convertGoal(self, goal: Goal):
        return {
            'name': goal.name,
            'partialGoals': self.convertPartialGoals(goal.partialgoal_set.all()),
            'records': self.convertRecords(goal.goalrecord_set.all())
        }

    def convertPartialGoals(self, partial_goals: List[PartialGoal]):
        return [partial_goal.value for partial_goal in partial_goals]

    def convertRecords(self, records: List[GoalRecord]):
        return [(record.value, record.date) for record in records]