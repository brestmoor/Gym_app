from collections import OrderedDict
from typing import Dict, List

from django.db import models

from Gym_app.business_logic.util.deep_model_to_dict import DeepMapper


class DjangoObjectsMapper:
    def __init__(self):
        self.mapper = DeepMapper()

    def map(self, collection):
        if isinstance(collection, models.Model):
            return self.mapper.model_to_dict(collection)

        if isinstance(collection, Dict):
            newDict = OrderedDict()
            for key in collection:
                newDict[key] = self.map(collection[key])
            return newDict

        if isinstance(collection, List):
            newList = []
            for i, value in enumerate(collection):
                newList.insert(i, self.map(collection[i]))
            return newList
