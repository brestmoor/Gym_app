from django.contrib import admin

from Gym_app.models import Class
from Gym_app.models import ClassInSchedule
from Gym_app.models import ClassInformation


# Register your models here.


class ClassModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'class_in_schedule')


admin.site.register(Class, ClassModelAdmin)


class ClassInScheduleModelAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time', 'class_type')


admin.site.register(ClassInSchedule, ClassInScheduleModelAdmin)


class ClassInformationModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(ClassInformation, ClassInformationModelAdmin)
