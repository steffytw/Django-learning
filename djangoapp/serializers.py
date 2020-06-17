from rest_framework import serializers
from . import models


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'    # or  ('id','name','age','address','gender')
        model = models.student