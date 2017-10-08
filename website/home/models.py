from django.db import models

class symptoms(models.Model):
    GENDER_CHOICES = (
        ('1', 'Male'),
        ('0', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    restbp = models.IntegerField()
    chol = models.IntegerField()
    durationexercise = models.IntegerField()
    maxHeartRate = models.IntegerField()

class diabSymp(models.Model):
    insulinDose = models.IntegerField()
    prebreakfastglucose = models.IntegerField()
    postbreakfastglucose = models.IntegerField()
    exerciseactivity = models.IntegerField()
    specialEvent = models.CharField(max_length=100)

