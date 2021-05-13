import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin 

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def is_published(self, obj):
        return obj.publish_date is not None
    is_published.boolean = True
    is_published.admin_order_field = '-publish_date'
    is_published.short_description = 'Is Published?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text