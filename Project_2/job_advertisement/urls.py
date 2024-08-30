from django.urls import path
from job_advertisement.views import ListJobAdvertisementAPIView

urlpatterns = [
    path('', ListJobAdvertisementAPIView.as_view())
]