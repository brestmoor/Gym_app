from collections import OrderedDict
from typing import Dict, List

from django.contrib.auth.models import User
from django.db import models
from itertools import chain

from django.db.models import ForeignKey
from Gym_app.business_logic.util.deep_model_to_dict import DeepMapper
from Gym_app.converters.MemberToDtoConverter import MemberToDtoConverter
from Gym_app.converters.UserToDtoConverter import UserToDtoConverter
from Gym_app.models import Member


class DjangoObjectsMapper:
    def __init__(self, should_user_to_email = None, should_member_basic_info = None):
        self.mapper = DeepMapper()
        self.user_converter = UserToDtoConverter()
        self.member_converter = MemberToDtoConverter()
        self.should_user_to_email = should_user_to_email
        self.should_member_basic_info = should_member_basic_info

    def map(self, collection):
        if self.should_member_basic_info:
            if isinstance(collection, Member):
                return self.member_converter.convert(collection)

        if self.should_user_to_email:
            if isinstance(collection, User):
                return collection.email

        if isinstance(collection, int):
            return collection

        if isinstance(collection, str):
            return collection

        if isinstance(collection, Member):
            return self.user_converter.convert(collection)

        if isinstance(collection, Member):
            return self.user_converter.convert(collection)

        if isinstance(collection, models.Model):
            return self.model_to_dict(collection)

        if isinstance(collection, Dict):
            newDict = OrderedDict()
            for key in collection:
                newDict[key] = self.map(collection[key])
            return newDict

        if isinstance(collection, List) or isinstance(collection, models.QuerySet):
            newList = []
            for i, value in enumerate(collection):
                newList.insert(i, self.map(collection[i]))
            return newList

    def model_to_dict(self, instance, fields=None, exclude=None):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
            if not getattr(f, 'editable', False):
                continue
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, ForeignKey):
                data[f.name] = self.map(f.related_model.objects.filter(pk=f.value_from_object(instance))[0]) if f.related_model.objects.filter(pk=f.value_from_object(instance)).exists() else None
                continue
            if isinstance(f, models.ManyToManyField):
                data[f.name] = self.map(f.value_from_object(instance))
                continue
            data[f.name] = f.value_from_object(instance)
        return data
