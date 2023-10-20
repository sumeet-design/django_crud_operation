from rest_framework.serializers import ModelSerializer
from .models import studentDetails


class QueryPracticeViewSerializers(ModelSerializer):
    class Meta:
        model = studentDetails
        fields = '__all__'
