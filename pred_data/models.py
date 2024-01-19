from django.db import models


GENDER_CHOICES = [(1, 'male'), (0, 'female')]

class Data(models.Model):
    age = models.IntegerField(blank = True ,null = True)
    gender = models.IntegerField(choices = GENDER_CHOICES)
    chest_pain = models.IntegerField(blank = True ,null = True)
    resting_bp = models.IntegerField(blank = True ,null = True)
    cholesterol = models.IntegerField(blank = True ,null = True)
    fasting_blood_suger = models.IntegerField(blank = True ,null = True)
    resting_ecg = models.IntegerField(blank = True ,null = True)
    max_heart_rate = models.IntegerField(blank = True ,null = True)
    exercise_angina = models.IntegerField(blank = True ,null = True)
    oldpeak = models.IntegerField(blank = True ,null = True)
    ST_slope = models.IntegerField(blank = True ,null = True)

class Prediction(models.Model):
    data = models.OneToOneField( Data, on_delete= models.CASCADE, primary_key=True, null = False, blank = True)
    prediction = models.IntegerField()