from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question = models.CharField(max_length=250)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    option1_votes = models.IntegerField(default=0)
    no_of_votes = models.IntegerField(default=0)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.question
