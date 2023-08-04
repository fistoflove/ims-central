from django.contrib import admin
from .models import Website, MaintenancePlan, MaintenanceTask, MaintenanceTaskList, MaintenanceTaskCategory, MaintenanceGrade, WebsiteEvent, Tag

admin.site.register(Website)
admin.site.register(MaintenancePlan)
admin.site.register(MaintenanceTaskList)
admin.site.register(MaintenanceTask)
admin.site.register(MaintenanceTaskCategory)
admin.site.register(MaintenanceGrade)
admin.site.register(WebsiteEvent)
admin.site.register(Tag)