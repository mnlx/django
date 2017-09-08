from rest_framework import serializers
from .models import *

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceField
        fields = ('extends', 'name')
