from rest_framework import viewsets
from job_advertisement.models import JobAdvertisement
from .serializer import JobAdvertisementSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView

class JobAdvertisementViewSets(viewsets.ModelViewSet):
    queryset = JobAdvertisement.objects.all()
    serializer_class = JobAdvertisementSerializer

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ListJobAdvertisementAPIView(ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = JobAdvertisement.objects.all()
    serializer_class = JobAdvertisementSerializer