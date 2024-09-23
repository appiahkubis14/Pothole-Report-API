from django.urls import path
from .views import PotholeReportView

urlpatterns = [
    path('pothole-reports/', PotholeReportView.as_view(), name='pothole-reports'),
]
