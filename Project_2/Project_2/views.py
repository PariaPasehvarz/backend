from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from job_advertisement.models import JobAdvertisement
from rest_framework.response import Response

class ApplyForJobAPIView(CreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, job_title):
        try:
            job_add = JobAdvertisement.objects.get(title = job_title)
        except JobAdvertisement.DoesNotExist:
            return Response({"msg": "Job Advertisement not found"})
        
        job_add.applicants.add(request.user)
        return Response({"msg": "Application successful!"})

