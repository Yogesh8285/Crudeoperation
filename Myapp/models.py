from django.db import models
class Education(models.Model):
    education = models.CharField(max_length=10)
    def __str__(self):
        return self.education
# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    Birth_date = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    education = models.ForeignKey(Education,on_delete= models.CASCADE)
    password = models.CharField(max_length=10)
