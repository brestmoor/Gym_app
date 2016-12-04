from rest_framework import serializers

from Gym_app.models import Class


class classSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
