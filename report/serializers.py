from rest_framework import serializers
from .models import PotholeReport

class PotholeReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotholeReport
        fields = [
            'ai_description',
            'alternate_description',
            'location_lat',
            'location_lon',
            'town_name',
            'road_type',
            'road_name',
            'origin',
            'destination',
            'image_url',
            'video_url',
            'timestamp',
        ]
        read_only_fields = ['timestamp']
