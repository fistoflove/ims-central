from datetime import date, datetime, timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from slugify import slugify

class Tag(models.Model):
    name = models.CharField(max_length=255) 
    def __str__(self):
        return self.name

@deconstructible
class RequireHttpOrHttpsUrl:
    def __call__(self, value):
        if not value.startswith("http://") and not value.startswith("https://"):
            raise ValidationError('Please provide a http or https resource')
        
class MaintenanceTaskCategory(models.Model):
    name = models.CharField(max_length=200, default='TASK CATEGORY NAME')
    description = models.TextField(blank = True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Maintenance Task Categories"
    
class MaintenanceTaskList(models.Model):
    name = models.CharField(max_length=200, default='TASK LIST NAME')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Maintenance Task Lists"

class MaintenanceTask(models.Model):
    name = models.CharField(max_length=200, default='TASK NAME')
    description = models.TextField(blank = True)
    task_list = models.ManyToManyField(MaintenanceTaskList)
    category = models.ForeignKey(MaintenanceTaskCategory, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name

    def slug(self):
        return slugify(self.name)
        
    class Meta:
        verbose_name_plural = "Maintenance Tasks"

class MaintenancePlan(models.Model):
    name = models.CharField(max_length=200, default='PLAN NAME')
    default_task_list = models.ForeignKey(MaintenanceTaskList, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Maintenance Plans"

class MaintenanceGrade(models.Model):
    name = models.CharField(max_length=200, default='A')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Website Maintenance Grades"

class Website(models.Model):
    name = models.CharField(max_length=200,  default='Website Name')
    description = models.TextField(blank = True)
    notes = models.TextField(blank = True)
    url = models.URLField(
        max_length=500, null=True,
        validators=[RequireHttpOrHttpsUrl()]
    )
    login_url = models.URLField(
        max_length=500, null=True, blank=True,
        validators=[RequireHttpOrHttpsUrl()]
    )
    testing_url = models.URLField(
        max_length=500, null=True, blank=True,
        validators=[RequireHttpOrHttpsUrl()]
    )
    maintenance_plan = models.ForeignKey(MaintenancePlan, on_delete=models.CASCADE, blank=True, null=True)
    maintenance_grade = models.ForeignKey(MaintenanceGrade, on_delete=models.CASCADE, blank=True, null=True)    
    maintenance_task_list = models.ForeignKey(MaintenanceTaskList, on_delete=models.CASCADE, blank=True, null=True)
    
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.name
    
    def days_since_maintenance(self):
        last_maintenance = WebsiteEvent.objects.filter(name="maintenance", website=self)
        if(len(last_maintenance) > 0):
            dslm = datetime.now(timezone.utc) - last_maintenance.last().created_at
            return dslm.days
        else:
            return 365

class WebsiteEvent(models.Model):
    name = models.CharField(max_length=200, default='Event Name')
    website = models.ForeignKey(Website, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    worker = models.CharField(max_length=200, default='Worker Name')
    data = models.JSONField(blank=True, null=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Website Events"

