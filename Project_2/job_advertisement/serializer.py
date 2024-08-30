from rest_framework import serializers
from job_advertisement.models import JobAdvertisement

class JobAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAdvertisement
        fields = 'title', 'image', 'expire_time', 'job_category', 'salary', 'insurance', 'working_time', 'applicants', 'owner'
        read_only_fields = ['owner']

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data.pop('owner', None)
        return super().update(instance, validated_data)