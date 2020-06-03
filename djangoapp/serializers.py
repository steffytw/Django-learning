from rest_framework import serializers
from .import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','name','age','address','gender')
        model = models.student