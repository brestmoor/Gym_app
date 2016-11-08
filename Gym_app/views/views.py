# -*- coding: utf-8 -*-

from django.core import serializers
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from Gym_app.business_logic.week import WeekInfoProvider
from Gym_app.models import Goal
from Gym_app.serializers import GoalSerializer
import json

class DayOfWeekNamesView(APIView):
    def get(self, request, format=None):
        week_days_names = WeekInfoProvider().get_current_week_days()
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
