from django import forms

class MaintenanceForm(forms.Form):
    task_data = forms.JSONField(widget=forms.HiddenInput())