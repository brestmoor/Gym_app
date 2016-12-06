# -*- coding: utf-8 -*-

import json

from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from Gym_app.business_logic.schedule.schedule_provider import ScheduleProvider
from Gym_app.business_logic.schedule.week_info_provider import WeekInfoProvider
from Gym_app.business_logic.util.date_serializer import DateSerializer
from Gym_app.business_logic.util.django_objects_serializer import DjangoObjectsMapper
from Gym_app.dao.user.UserDao import UserDao
from Gym_app.models import Goal
from Gym_app.serializers.goal_serializers import GoalSerializer
from Gym_app.validators.UserRegistrationValidator import UserRegistrationValidator


class DayOfWeekNamesView(APIView):
    def get(self, request, format=None):
        week_days_names = WeekInfoProvider().get_current_days_of_the_week()
        for day in week_days_names:
            day.encode("UTF-8")
        return Response(json.dumps(week_days_names))


class GoalsListView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class GoalsSingleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class GoalsViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class HomePageView(TemplateView):
    template_name = "index.html"


class ScheduleView(APIView):
    def get(self, request, format=None):
        schedule = ScheduleProvider().get_current_schedule()
        prepared = DjangoObjectsMapper().map(schedule)
        return HttpResponse(json.dumps(prepared, default=DateSerializer.serialize))


class UserView(APIView):
    def post(self, request, format=None):
        try:
            UserRegistrationValidator().validate(request.data)
        except ValidationError as error:
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        user_dao = UserDao()
        user_dao.insert(request.data)
        return HttpResponseRedirect('/schedule', status=status.HTTP_201_CREATED)


class SessionView(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(json.dumps({'name': user.first_name, 'lastName': user.last_name}), status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
