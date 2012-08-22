import datetime
from django.db import models
from django.utils import timezone

AUDIENCE_CHOICES  = [
    ('corp', 'Corporate Users'),
    ('pub', 'Public Users'),
    ]

class Poll(models.Model):
    question = models.CharField(max_length=128)
    pub_date = models.DateTimeField(verbose_name='Data Published', auto_now_add=True)
    last_updated = models.DateTimeField(verbose_name='Last Updated', auto_now=True)
    audience = models.CharField(max_length=8, choices=AUDIENCE_CHOICES)
    frequency = models.FloatField(verbose_name='Display Frequency',
                help_text='Controls how frequently a given poll is displayed to users')
    
    def __str__(self):
        return self.question
    
    def was_published_recently(self):
        return self.pub_date
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=129)
    votes = models.IntegerField()