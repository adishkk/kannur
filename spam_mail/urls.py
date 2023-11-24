"""spam_mail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from siteAdmin import views as adminview
from User import views as userview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',adminview.index,name='index'),
    path('userRegistration/',userview.userRegistration,name='userRegistration'),
    path('getstate/',userview.getstate,name='getstate'),
    path('userRegistrationAction/',userview.userRegistrationAction,name='userRegistrationAction'),
    path('login/',adminview.login,name='login'),
    path('loginAction/',adminview.loginAction,name='loginAction'),
    path('season/',adminview.season,name='season'),
    path('seasonAction/',adminview.seasonAction,name='seasonAction'),
    path('seasonFactor/',adminview.seasonFactor,name='seasonFactor'),
    path('seasonFactorAction/',adminview.seasonFactorAction,name='seasonFactorAction'),
    path('hobbyFactor/',adminview.hobbyFactor,name='hobbyFactor'),
    path('hobbyFactorAction/',adminview.hobbyFactorAction,name='hobbyFactorAction'),
    path('seasonCountry/',adminview.seasonCountry,name='seasonCountry'),
    path('getFactor/',adminview.getFactor,name="getFactor"),
    path('getstate/',adminview.getstate,name='getstate'),
    path('seasonCountryAction/',adminview.seasonCountryAction,name='seasonCountryAction'),
    path('agefactor/',adminview.agefactor,name='agefactor'),
    path('agefactorAction/',adminview.agefactorAction,name='agefactorAction'),
    path('message/',userview.message,name='message'),
    path('messageAction/',userview.messageAction,name='messageAction'),
    path('checkUsername/',userview.checkUsername,name='checkUsername'),
    path('sendMessage/',userview.sendMessage,name='sendMessage'),
    path('deletemsg/<int:id>/',userview.deletemsg,name='deletemsg'),
    path('Userinbox/',userview.Userinbox,name='Userinbox'),
    path('msgTrash/',userview.msgTrash,name='msgTrash'),
    path('viewTrash/',userview.viewTrash,name='viewTrash'),
    path('deleteMessage/<int:id>',userview.deleteMessage,name='deleteMessage'),
    path('forwardMessage/<int:id>',userview.forwardMessage,name='forwardMessage'),
    path('forwardMessageAction/',userview.forwardMessageAction,name='forwardMessageAction'),
    path('replayMessage/<int:id>',userview.replayMessage,name='replayMessage'),
    path('replayMessageAction/',userview.replayMessageAction,name='replayMessageAction'),
    path('contact/',userview.contact,name='contact'),
    path('contactAtion/',userview.contactAtion,name='contactAtion'),
    path('contactView/',userview.contactView,name='contactView'),
    path('deleteContact/<int:id>',userview.deleteContact,name='deleteContact'),
    path('blacklistContact/',userview.blacklistContact,name='blacklistContact'),
    path('blacklistContactAction/',userview.blacklistContactAction,name='blacklistContactAction'),
    path('viewBlacklist/',userview.viewBlacklist,name='viewBlacklist'),
    path('deleteBlacklist/<int:id>',userview.deleteBlacklist,name='deleteBlacklist'),
    path('blacklistContactMove/<int:id>',userview.blacklistContactMove,name='blacklistContactMove'),
    path('customerFactor/',userview.customerFactor,name='customerFactor'),
    path('gethobby/',userview.gethobby,name='gethobby'),
    path('customerHobby/',userview.customerHobby,name='customerHobby'),
    path('ageFactor/',userview.ageFactor,name='ageFactor'),
    path('ageFactorAction/',userview.ageFactorAction,name='ageFactorAction'),
    path('customerSeason/',userview.customerSeason,name='customerSeason'),
    path('customerSeasonAction/',userview.customerSeasonAction,name='customerSeasonAction'),
    path('viewSpam/',userview.viewSpam,name='viewSpam'),
    path('deleteSpam/<int:id>',userview.deleteSpam,name='deleteSpam'),
    path('Editprofile/',userview.Editprofile,name='Editprofile'),
    path('getstate/',userview.getstate,name='getstate'),
    path('editprofileAction/',userview.editprofileAction,name='editprofileAction'),
    path('forgotPassword/',adminview.forgotPassword,name='forgotPassword'),
    path('forgotPasswordAction/',adminview.forgotPasswordAction,name='forgotPasswordAction'),
    path('newpasswordAction/',adminview.newpasswordAction,name='newpasswordAction'),
    path('updatePasswordAction/',adminview.updatePasswordAction,name='updatePasswordAction'),
    path('logout/',adminview.logout,name='logout')
    

]
