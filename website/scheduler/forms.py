from django import forms
from .models import Practice, Band
from datetime import datetime, time

class PracticeForm(forms.ModelForm):
    band = forms.ModelChoiceField(queryset=Band.objects.filter(event__date__gt=datetime.now().date()))
    class Meta:
        model = Practice
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={'type':'date'}),
            'startTime': forms.TimeInput(attrs={'type':'time'}),
            'endTime': forms.TimeInput(attrs={'type':'time'}),
        }
    
    def clean(self): #Overrided clean method for additional validation
        cleaned_data = super(PracticeForm, self).clean()
        start = cleaned_data.get('startTime')
        end = cleaned_data.get('endTime')
        date = cleaned_data.get('date')

        if start > end: 
            raise forms.ValidationError("Start time cannot be later than end time!")

        if date < datetime.now().date():
            raise forms.ValidationError("Error, cannot book a practice in the past")
        
        if start < time(8,0):
            raise forms.ValidationError("Error, don't book a practice before 7am, I (Avi) am not waking up!")

        conflicts = Practice.objects.filter(
                date=date,
                startTime__lt=end, #filter for any practices with startTime < endTime of this practice
                endTime__gt=start, #filter for any practices with endTime > startTime of this practice
            ).exclude(
                id=self.instance.id
            )
        if any(conflicts): #conflict validation 
            st = "Room is booked from "
            for i in conflicts:
                st += f"{i.startTime} to {i.endTime}, "
            raise forms.ValidationError(f"Conflict! {st}")
        return cleaned_data
