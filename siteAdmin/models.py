from django.db import models

# Create your models here.
class AdminModel(models.Model):
    Username=models.CharField(max_length=255)
    Password=models.CharField(max_length=255)


class HobbyModel(models.Model):
    Name=models.CharField(max_length=255)

class SeasonModel(models.Model):
    Name=models.CharField(max_length=255)

class SeasonFactorModel(models.Model):
    Season=models.ForeignKey(SeasonModel,on_delete=models.CASCADE)
    Factor_Name=models.CharField(max_length=255)

class HobbyFactorModel(models.Model):
    Hobby=models.ForeignKey(HobbyModel,on_delete=models.CASCADE)
    Factor_Name=models.CharField(max_length=255)

class SeasonCountryModel(models.Model):
    Season=models.ForeignKey(SeasonModel,on_delete=models.CASCADE)
    Country=models.ForeignKey('User.CountryModel',on_delete=models.CASCADE)
    State=models.ForeignKey('User.StateModel',on_delete=models.CASCADE)
    Factor=models.ForeignKey(SeasonFactorModel,on_delete=models.CASCADE)
    Months=models.IntegerField()

class AgefactorModel(models.Model):
    Min_age=models.IntegerField()
    Max_age=models.IntegerField()
    Factor=models.CharField(max_length=255)

