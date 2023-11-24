from django.db import models

# Create your models here.

class CountryModel(models.Model):
    Name=models.CharField(max_length=255)

class StateModel(models.Model):
    Name=models.CharField(max_length=255)
    Country=models.ForeignKey(CountryModel,on_delete=models.CASCADE)

class UserRegistrationModel(models.Model):
    Name=models.CharField(max_length=255)
    DOB=models.CharField(max_length=25)
    Gender=models.CharField(max_length=50)
    Address=models.CharField(max_length=255)
    Phone=models.CharField(max_length=50)
    Security_question=models.CharField(max_length=500)
    Answer=models.CharField(max_length=500)
    Username=models.CharField(max_length=500)
    Password=models.CharField(max_length=255)
    State=models.ForeignKey(StateModel,on_delete=models.CASCADE)
    Country=models.ForeignKey(CountryModel,on_delete=models.CASCADE)

class UserHobbyModel(models.Model):
    User=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE)
    Hobbies=models.ForeignKey('siteAdmin.HobbyModel',on_delete=models.CASCADE)

class MessageModel(models.Model):
    Sender=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,related_name='Sender')
    Receiver=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,related_name='Receiver')
    Subject=models.CharField(max_length=255)
    Message=models.CharField(max_length=500)
    Date=models.CharField(max_length=50)
    Time=models.CharField(max_length=50)
    Status=models.CharField(max_length=50,default='pending')
    Filter_status=models.CharField(max_length=50,default='pending')

class TrashModel(models.Model):
    Receiver=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE)
    Message=models.ForeignKey(MessageModel,on_delete=models.CASCADE)
    Date=models.CharField(max_length=50)
    Time=models.CharField(max_length=50)


class ContactModel(models.Model):
    User=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,related_name='user')
    Contact=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,related_name='contact')
    Remarks=models.CharField(max_length=500,default='abc')
    Name=models.CharField(max_length=255)
    Date=models.CharField(max_length=50)
    Time=models.CharField(max_length=50)

class BlackListModel(models.Model):
    User=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,related_name='user1')
    Contact=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE,related_name='contact1')
    Remarks=models.CharField(max_length=500,default='abc')
    Name=models.CharField(max_length=255)
    Date=models.CharField(max_length=50)
    Time=models.CharField(max_length=50)

class CustomerHobbyModel(models.Model):
    User=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE)
    Hobby=models.ForeignKey('siteAdmin.HobbyModel',on_delete=models.CASCADE)
    Factor=models.ForeignKey('siteAdmin.HobbyFactorModel',on_delete=models.CASCADE)


class CustomerAgeFactorModel(models.Model):
    User=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE)
    Factor=models.ForeignKey('siteAdmin.AgefactorModel',on_delete=models.CASCADE)

class CustomerSeasonCountryModel(models.Model):
    User=models.ForeignKey(UserRegistrationModel,on_delete=models.CASCADE)
    Factor=models.ForeignKey('siteAdmin.SeasonFactorModel',on_delete=models.CASCADE)
    
