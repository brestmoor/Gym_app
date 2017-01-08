from django.contrib import admin

from Gym_app.models import Exercise
from Gym_app.models import ExerciseInPlan
from Gym_app.models import Goal
from Gym_app.models import GoalRecord
from Gym_app.models import GroupClass
from Gym_app.models import ClassInSchedule
from Gym_app.models import ClassInformation

# Register your models here.
from Gym_app.models import PartialGoal
from Gym_app.models import TrainingPlan
from Gym_app.models.classes_models import PersonalTraining


class ClassModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'class_in_schedule')


admin.site.register(GroupClass, ClassModelAdmin)


class ClassInScheduleModelAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time', 'class_type')


admin.site.register(ClassInSchedule, ClassInScheduleModelAdmin)


class ClassInformationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(ClassInformation, ClassInformationModelAdmin)


class PersonalTrainingModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'class_in_schedule')


admin.site.register(PersonalTraining, PersonalTrainingModelAdmin)


class ExerciseInPlanModelAdmin(admin.ModelAdmin):
    list_display = ('plan', 'exercise','day','order','repetitions')


admin.site.register(ExerciseInPlan, ExerciseInPlanModelAdmin)

class TrainingPlanModelAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'description')

admin.site.register(TrainingPlan, TrainingPlanModelAdmin)


class ExerciseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')

admin.site.register(Exercise, ExerciseModelAdmin)


class GoalModelAdmin(admin.ModelAdmin):
    list_display = ('member', 'name')

admin.site.register(Goal, GoalModelAdmin)


class PartialGoalModelAdmin(admin.ModelAdmin):
    list_display = ('goal', 'value')

admin.site.register(PartialGoal, PartialGoalModelAdmin)


class GoalRecordModelAdmin(admin.ModelAdmin):
    list_display = ('goal', 'date', 'value')

admin.site.register(GoalRecord, GoalRecordModelAdmin)
