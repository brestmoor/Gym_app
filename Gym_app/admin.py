from django.contrib import admin

from Gym_app.models import GroupClass
from Gym_app.models import ClassInSchedule
from Gym_app.models import ClassInformation


# Register your models here.
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
