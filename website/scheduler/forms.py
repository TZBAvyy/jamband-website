from django import forms
from .models import Practice, Band


class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'startTime': forms.TimeInput(attrs={'type':'time'}),
            'endTime': forms.TimeInput(attrs={'type':'time'}),
        }
