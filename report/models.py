from django.db import models

class PotholeReport(models.Model):
    ai_description = models.TextField(default='N/A')
    alternate_description = models.TextField(default='N/A')
    location_lat = models.DecimalField(max_digits=12, decimal_places=10, null=True, blank=True)
    location_lon = models.DecimalField(max_digits=12, decimal_places=10, null=True, blank=True)
    town_name = models.CharField(max_length=255,blank=True)
    road_type = models.CharField(max_length=255,blank=True)
    road_name = models.CharField(max_length=255,  blank=True)
    origin = models.CharField(max_length=255,blank=True,null=True)
    destination = models.CharField(max_length=255,blank=True,null=True)
    image_url = models.ImageField(upload_to='images/', null=True, blank=True)
    video_url = models.FileField(upload_to='videos/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Pothole Report: {self.road_name}, {self.town_name}'
