from Gym_app.dao.ExercisesDao import ExercisesDao
from Gym_app.models import ExerciseInPlan


class ExerciseInPlanDao:
    def createMultiple(self, exercisesInPlan, plan):
        for exerciseInPlan in exercisesInPlan:
            new_exercise_in_plan = ExerciseInPlan()
            new_exercise_in_plan.day = exerciseInPlan['day']
            new_exercise_in_plan.exercise = ExercisesDao().get_by_name(exerciseInPlan['exercise'])
            new_exercise_in_plan.order = exerciseInPlan['order']
            new_exercise_in_plan.repetitions = exerciseInPlan['repetitions']
            new_exercise_in_plan.plan = plan
            new_exercise_in_plan.save()