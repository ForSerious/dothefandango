from __future__ import unicode_literals
import time
from django.db import models

# Create your models here.
def aNumber():
    sTime = time.strftime("%S")
    iNum = int(sTime)
    return str(iNum * 3)
    
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)