from django.db import models

# Create your models here.
from django.db import models

class PassengerData(models.Model):
    PassengerId = models.IntegerField(primary_key=True)
    Pclass = models.IntegerField()
    Name = models.CharField(max_length=255)
    Sex = models.CharField(max_length=10)
    Age = models.FloatField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField(default=0)
    Ticket = models.CharField(max_length=255)
    Fare = models.FloatField()
    Cabin = models.CharField(max_length=50, null=True, blank=True)
    Embarked = models.CharField(max_length=10)
