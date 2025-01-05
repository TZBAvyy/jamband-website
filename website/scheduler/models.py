from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Practice(models.Model):
    band = models.ForeignKey('Band', models.CASCADE, null=False, related_name='practices')
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()

    class Meta:
        ordering = ['date', 'startTime']

    def __str__(self):
        return f"[{self.date}] {self.band} from {self.startTime} to {self.endTime}"
    
class Event(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Event name must be greater than 1 character")]
    )
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ['-date','-time']

    def __str__(self):
        return self.name
    
class Band(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Event name must be greater than 1 character")]
    )
    event = models.ForeignKey('Event', models.CASCADE, null=False, related_name='bands')
    members = models.ManyToManyField('Member', related_name='bands', blank=True)
    band_no = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Member(models.Model):
    name = models.CharField(
            max_length=50, 
            help_text='Enter a member\'s full name (e.g. Avi)',
            validators=[MinLengthValidator(2, "Member name must be greater than 1 character")]
    )

    def __str__(self):
        return self.name
    
