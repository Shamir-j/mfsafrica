from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Point
        fields = ['id', 'points', 'closetpointpair', 'closetdistance', 'createdDate']

        def __str___(self):
            return self.points