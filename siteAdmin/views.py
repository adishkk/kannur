from django.shortcuts import render,redirect
from User.models import *
from siteAdmin.models import *
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def loginAction(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        admin_db=AdminModel.objects.filter(Username=username,Password=password)
        user_db=UserRegistrationModel.objects.filter(Username=username,Password=password)
        if admin_db.count()>0:
            request.session['id']=admin_db[0].id
            return render(request,'AdminHome.html')
        elif user_db.count()>0:
            request.session['id']=user_db[0].id
            print(request.session['id'])
            request.session['Username']=username
            # request.session['id']=user_db[0].Username
            # print(request.session['Username'])
            # print(user)
            return render(request,'userHome.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def season(request):
    return render(request,'season.html')

def seasonAction(request):
    name=request.POST['season']
    season_db=SeasonModel(Name=name)
    season_db.save()
    return render(request,'season.html')


def seasonFactor(request):
    season_db=SeasonModel.objects.all()
    return render(request,'seasonFactor.html',{'season':season_db})

def seasonFactorAction(request):
    season=request.POST['season']
    name=request.POST['name']
    factor_db=SeasonFactorModel(Factor_Name=name,Season_id=season)
    factor_db.save()
    return redirect('seasonFactor')

def hobbyFactor(request):
    hobby_db=HobbyModel.objects.all()
    return render(request,'hobbyFactor.html',{'hobby':hobby_db})

def hobbyFactorAction(request):
    hobby=request.POST['hobby']
    name=request.POST['name']
    factor_db=HobbyFactorModel(Factor_Name=name,Hobby_id=hobby)
    factor_db.save()
    return redirect('hobbyFactor')

def seasonCountry(request):
    country_db=CountryModel.objects.all()
    season_db=SeasonModel.objects.all()
    return render(request,'seasonCountry.html',{'country':country_db,'season':season_db})

def getFactor(request):
    sid=request.GET['season']
    factor_db=SeasonFactorModel.objects.filter(Season=sid)
    return render(request,'getFactor.html',{'factor':factor_db})

def getstate(request):
    cid=request.GET['country']
    state_db=StateModel.objects.filter(Country=cid)
    return render(request,'getstate.html',{'state':state_db})

def seasonCountryAction(request):
    season=request.POST['season']
    print(season)
    factor=request.POST['factor']
    print(factor)
    country=request.POST['country']
    print(country)
    state=request.POST['state']
    print(state)
    months=request.POST['months']
    print(months)
    seasoncountry_db=SeasonCountryModel(Months=months,Country_id=country,Factor_id=factor,Season_id=season,State_id=state)
    seasoncountry_db.save()
    messages.add_message(request,messages.INFO,"Added Succesfully")

    return redirect('seasonCountry')

def agefactor(request):
    return render(request,'agefactor.html')

def agefactorAction(request):
    min=request.POST['min_age']
    max=request.POST['max_age']
    factor=request.POST['name']
    age_db=AgefactorModel(Min_age=min,Max_age=max,Factor=factor)
    age_db.save()
    messages.add_message(request,messages.INFO,"Added Succesfully")

    return redirect('agefactor')


def forgotPassword(request):
    return render(request,'forgotpasswordusername.html')


def forgotPasswordAction(request):
    username=request.POST.get('username')
    user_db=UserRegistrationModel.objects.filter(Username=username)
    country_db=CountryModel.objects.all()
    if user_db.count()>0:
        return render(request,'newpassword.html',{'data':username,'country':country_db})
    else:
        return render(request,'forgotpasswordusername.html')


def newpasswordAction(request):
    username=request.POST['username']
    country=request.POST['country']
    dob=request.POST['dob']
    user_db=UserRegistrationModel.objects.filter(Username=username,Country_id=country,DOB=dob)
    if user_db.count()>0:
        request.session=user_db[0].id
        return render(request,'updatePassword.html',{'data':user_db})
    else:
        return render(request,'newpassword.html')

def updatePasswordAction(request):
    # username=request.POST['username']
    user_id=request.session['id']
    password=request.POST['password']
    repass=request.POST['repass']
    if password==repass:
        user_db=UserRegistrationModel.objects.filter(id=user_id)
        user_db.update(Password=password)
        return render(request,'login.html')

def logout(request):
    request.session.clear()
    return redirect('index')



        

