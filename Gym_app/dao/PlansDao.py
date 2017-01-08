from django.contrib.auth.models import Group

from Gym_app.business_logic.personal_training.grouper import Grouper
from Gym_app.dao.ExerciseInPlanDao import ExerciseInPlanDao
from Gym_app.dao.InstructorDao import InstructorDao
from Gym_app.models import Member
from Gym_app.models import TrainingPlan


class PlansDao:
    def getAll(self):
        plans = TrainingPlan.objects.values_list('description', 'id')
        result = []
        for plan in plans:
            result.append({
                'id': plan[1],
                'description': plan[0]
            })
        return result

    def getByIdWithGroupedExercises(self, id):
        grouper = Grouper()
        plan = TrainingPlan.objects.get(pk=id)
        return grouper.group(list(plan.exerciseinplan_set.all()))

    def getById(self, id):
        return TrainingPlan.objects.get(pk=id)

    def getByUser(self, email):
        user = Member.objects.get(username = email)
        plans = user.trainingplan_set.all()
        if plans is None:
            return []
        else:
            return plans

    def deleteById(self, id):
        TrainingPlan.objects.get(pk=id).delete()


    def createAndFill(self, exercises, name, email):
        new_plan = TrainingPlan()
        new_plan.description = name
        new_plan.trainer = InstructorDao().getByEmail(email)
        new_plan.save()
        ExerciseInPlanDao().createMultiple(exercises, new_plan)