import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('pub_date')

    ## done for the interactive shell , to give out the relevant information
    def __str__(self):
        return self.question_text

    ## if the question was pulished in less than a day
    def was_pulished_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text