# -*- coding: utf-8 -*-

import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from Gym_app.business_logic.personal_training.DietEnricher import DietEnricher
from Gym_app.business_logic.personal_training.LengthAdder import LengthAdder
from Gym_app.business_logic.personal_training.TrainingAttendanceManager import TrainingAttendanceManager
from Gym_app.business_logic.schedule.ClassAttendanceManager import ClassAttendanceManager
from Gym_app.business_logic.schedule.PersonalScheduleProvider import PersonalScheduleProvider
from Gym_app.business_logic.schedule.class_schedule_provider import GroupClassScheduleProvider
from Gym_app.business_logic.schedule.week_info_provider import WeekInfoProvider
from Gym_app.business_logic.util.django_objects_serializer import DjangoObjectsMapper
from Gym_app.dao.DietDao import DietDao
from Gym_app.dao.ExercisesDao import ExercisesDao
from Gym_app.dao.PlansDao import PlansDao
from Gym_app.dao.TrainingDao import TrainingDao
from Gym_app.dao.user.MemberDao import MemberDao
from Gym_app.models import Goal
from Gym_app.serializers.StandardSerializer import CustomSerializer
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


class PersonalTrainingsScheduleView(APIView):
    def get(self, request, format=None):
        schedule = PersonalScheduleProvider().get_current_schedule()
        prepared = DjangoObjectsMapper(True).map(schedule)
        return HttpResponse(json.dumps(prepared, default=CustomSerializer.serialize))


class GroupClassesScheduleView(APIView):
    def get(self, request, format=None):
        schedule = GroupClassScheduleProvider().get_current_schedule()
        prepared = DjangoObjectsMapper().map(schedule)
        return HttpResponse(json.dumps(prepared, default=CustomSerializer.serialize))


class ClassAttendanceView(APIView):
    @method_decorator(login_required)
    def post(self, request, class_number, format=None):
        cam = ClassAttendanceManager()
        cam.sign_up_for_class(class_number, request.user.email)
        classes_ids = cam.get_ids_for_user(request.user.email)
        attendees = cam.get_attendees_for_class(class_number)
        return HttpResponse(
            json.dumps({'classes': classes_ids, 'attendees': attendees}, default=CustomSerializer.serialize))

    @method_decorator(login_required)
    def delete(self, request, class_number, format=None):
        cam = ClassAttendanceManager()
        cam.resign_from_class(request.user.email, class_number)
        classes_ids = cam.get_ids_for_user(request.user.email)
        attendees = cam.get_attendees_for_class(class_number)
        return HttpResponse(
            json.dumps({'classes': classes_ids, 'attendees': attendees}, default=CustomSerializer.serialize))


class TrainingAttendanceView(APIView):
    @method_decorator(login_required)
    def post(self, request, class_number, format=None):
        tam = TrainingAttendanceManager()
        tam.sign_up_for_class(class_number, request.user.email)
        attendee_email = TrainingDao().get_training_by_id(class_number).attendee.email
        return HttpResponse(attendee_email)

    @method_decorator(login_required)
    def delete(self, request, class_number, format=None):
        tam = TrainingAttendanceManager()
        tam.resign_from_class(request.user.email, class_number)
        return HttpResponse()


class MyClassesView(APIView):
    @method_decorator(login_required)
    def get(self, request):
        cam = ClassAttendanceManager()
        if request.query_params.get('q') == '':
            prepared = DjangoObjectsMapper().map(cam.get_classes_for_user(request.user.email))
            return HttpResponse(json.dumps(prepared, default=CustomSerializer.serialize))
        if request.query_params.get('q') == 'ids':
            return HttpResponse(json.dumps(cam.get_ids_for_user(request.user.email)))


class UserView(APIView):
    def post(self, request, format=None):
        #       try:
        #            UserRegistrationValidator().validate(request.data)
        #      except ValidationError as error:
        #     return Response(error, status=status.HTTP_400_BAD_REQUEST)
        user_dao = MemberDao()
        user_dao.insert(request.data)
        return HttpResponseRedirect('/schedule', status=status.HTTP_201_CREATED)


class SessionView(APIView):
    def post(self, request, format=None):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(
                json.dumps({'name': user.first_name, 'lastName': user.last_name, 'email': user.username,
                            'isValidMember': True, 'group': user.groups.all()[0].name}),
                status=status.HTTP_200_OK)
        else:
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)


class TrainingPlansView(APIView):
    def get(self, request, id=None, format=None):
        if id is not None:
            plan = PlansDao().getByIdWithGroupedExercises(id)
            mappedPlan = DjangoObjectsMapper(True).map(plan)
            return HttpResponse(json.dumps(mappedPlan, default=CustomSerializer.serialize))
        else:
            plans = PlansDao().getAll()
            return HttpResponse(json.dumps(plans, default=CustomSerializer.serialize))

    def delete(self, request, id=None):
        if id is not None:
            plans_dao = PlansDao()
            plans_dao.deleteById(id)
            plans = plans_dao.getAll()
            return HttpResponse(json.dumps(plans, default=CustomSerializer.serialize))
        else:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        PlansDao().createAndFill(request.data['plan'], request.data['planName'], request.data['email'])
        return HttpResponse(status=status.HTTP_200_OK)


class TrainingPlansForUserView(APIView):
    def get(self, request, username, format=None):
        plan = PlansDao().getByUser(username)
        mappedPlan = DjangoObjectsMapper(True).map(plan)
        return HttpResponse(json.dumps(mappedPlan, default=CustomSerializer.serialize))


class ExercisesView(APIView):
    def get(self, username, format=None):
        exercises = ExercisesDao().getAll()
        exercisesMapped = DjangoObjectsMapper(True).map(exercises)
        return HttpResponse(json.dumps(exercisesMapped, default=CustomSerializer.serialize))


class DietsView(APIView):
    def get(self, request, id=None):
        if id is not None:
            diet = DietDao().getByIdWithGroupedMeals(id)
            diet_with_calories = DietEnricher().addCalories(diet)
            mapped_diet = DjangoObjectsMapper(True).map(diet_with_calories)
            return HttpResponse(json.dumps(mapped_diet, default=CustomSerializer.serialize))
        else:
            if request.query_params.get('email') is not None:
                diets = DietDao().getAllForTrainer(request.query_params.get('email'))
                diets_mapped = DjangoObjectsMapper(True).map(diets)
                return HttpResponse(json.dumps(diets_mapped, default=CustomSerializer.serialize))
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        DietDao().createAndFill(request.data['diet'], request.data['dietName'], request.data['email'])
        return HttpResponse(status=status.HTTP_200_OK)


class MembersView(APIView):
    def get(self, request, id=None):
        if id is not None:
            member_dao = MemberDao()
            django_objects_mapper = DjangoObjectsMapper(True, True)
            member = member_dao.get_by_id(id)
            mapped_member = django_objects_mapper.map(member)
            goal = member_dao.get_goal_for_member(member)
            mapped_goal = django_objects_mapper.map(goal)
            return HttpResponse(json.dumps(mapped_member, default=CustomSerializer.serialize))
        else:
            if request.query_params.get('email') is not None:
                members = MemberDao().get_all_for_trainer(request.query_params.get('email'))
                membersMapped = DjangoObjectsMapper(True, True).map(members)
                return HttpResponse(json.dumps(membersMapped, default=CustomSerializer.serialize))
            else:
                return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        MemberDao().update(request.data['member'])
        return HttpResponse(status=status.HTTP_200_OK)
