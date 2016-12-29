from rest_framework import serializers

from Gym_app.models import GroupClass


class classSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupClass
        fields = '__all__'
