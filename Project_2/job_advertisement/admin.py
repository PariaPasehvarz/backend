from django.contrib import admin
from job_advertisement.models import JobAdvertisement

class JobAdvertisementAdmin(admin.ModelAdmin):
    readonly_fields = ('owner', 'applicants',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner = request.user)
    
    def has_change_permission(self, request, obj= None):
        if obj is not None and obj.owner != request.user:
            return False
        return super().has_change_permission(request, obj)

    def save_model(self, request, obj, form , change):
        if not change:
            obj.owner = request.user
        obj.save()

admin.site.register(JobAdvertisement, JobAdvertisementAdmin)