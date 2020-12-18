from django.db import models

# Create your models here.

class Report(models.Model):
    name = models.CharField(max_length=50)
    age = models. IntegerField()
    gender = models.CharField(max_length=30)
    height = models. IntegerField()
    weight = models. IntegerField()
    symptom1 = models.CharField(max_length=30)
    symptom2 = models.CharField(max_length=30, blank=True)
    symptom3 = models.CharField(max_length=30, blank=True)
    symptom4 = models.CharField(max_length=30, blank=True)
    symptom5 = models.CharField(max_length=30, blank=True)
    disease = models.CharField(max_length=30)
    consultDoctor = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class description(models.Model):
    id = models.AutoField(primary_key=True)
    disease = models.CharField(max_length=250)
    description =models.TextField(max_length=5000)

    def __str__(self):
        return self.disease