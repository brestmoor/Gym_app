"""Gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from Gym_app.views import views

router = DefaultRouter()
router.register(r'goals', views.GoalsViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    # url(r'^goals/$', views.GoalsListView.as_view()),
    # url(r'^goals/(?P<pk>[0-9])/$', views.GoalsSingleView.as_view())
    url(r'^', include(router.urls)),
    url(r'^schedule/$', views.HomePageView.as_view()),
    url(r'^classes/', views.GoalsListView.as_view()),
    url(r'^schedule/days$', views.DayOfWeekNamesView.as_view()),
    url(r'^schedule/classes$', views.GroupClassesScheduleView.as_view()),
    url(r'^personalTraining/trainings$', views.PersonalTrainingsScheduleView.as_view()),
    url(r'^personalTraining/trainings/([0-9]+)/attendee$', views.TrainingAttendanceView.as_view()),
    url(r'^schedule/classes/([0-9]+)/attendees$', views.ClassAttendanceView.as_view()),
    url(r'^member/classes/', views.MyClassesView.as_view()),
    url(r'^users$', views.UserView.as_view()),
    url(r'^session$', views.SessionView.as_view()),
    url(r'^trainingPlans/$', views.TrainingPlansView.as_view()),
    url(r'^trainingPlans/([0-9]+)$', views.TrainingPlansView.as_view()),
    url(r'^trainingPlans/([\w.@+-]+)$', views.TrainingPlansForUserView.as_view()),
    url(r'^exercises/$', views.ExercisesView.as_view()),
    url(r'^diets/$', views.DietsView.as_view()),
    url(r'^diets/([0-9]+)$', views.DietsView.as_view()),
    url(r'^meals/$', views.DietsView.as_view()),
    url(r'^members/$', views.MembersView.as_view()),
    url(r'^members/([0-9]+)$', views.MembersView.as_view()),
    url(r'^members/([0-9]+)/records/$', views.MembersView.as_view()),
    url(r'^members/([0-9]+)/partialGoals/$', views.PartialGoalsView.as_view())
]
