from django.shortcuts import render,redirect
from User.models import *
from siteAdmin.models import *
from django.contrib import messages
import datetime
from django.http import JsonResponse
# Create your views here.
def userRegistration(request):
    country_db=CountryModel.objects.all()
    hobby_db=HobbyModel.objects.all()
    state_db=StateModel.objects.all()
    return render(request,'UserRegistration.html',{'state':state_db,'country':country_db,'hobby':hobby_db})
    
    
def getstate(request):
    cid=request.GET['country']
    state_db=StateModel.objects.filter(Country=cid)
    return render(request,'getstate.html',{'state':state_db})

def userRegistrationAction(request):
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    address=request.POST['address']
    phone=request.POST['phone']
    security=request.POST['question']
    answer=request.POST['answer']
    username=request.POST['username']
    password=request.POST['password']
    country=request.POST['country']
    state=request.POST['state']
    user_db=UserRegistrationModel(Name=name,DOB=dob,Gender=gender,Address=address,Phone=phone,Security_question=security,Answer=answer,Username=username+'@mymail.com',Password=password,Country_id=country,State_id=state)
    user_db.save()
    hobby=request.POST.getlist('hobby')
    for hid in hobby:
        hobby_db=UserHobbyModel(Hobbies_id=hid,User_id=user_db.id)
        hobby_db.save()
    messages.add_message(request,messages.INFO,"Registration Sucessful")
    return redirect('userRegistration')

def message(request):
    return render(request,'message.html')

def messageAction(request):
    sender=request.session['id']
    receiver=request.POST['name']
    rev=UserRegistrationModel.objects.get(Username=receiver)
    subject=request.POST['subject']
    msg=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    message_db=MessageModel(Subject=subject,Message=msg,Date=date,Time=time,Receiver=rev,Sender_id=sender)
    message_db.save()
    messages.add_message(request,messages.INFO,"Message Send")
    return redirect('message')

def checkUsername(request):
    name=request.GET['username']
    user_db=UserRegistrationModel.objects.filter(Username=name)
    if len(user_db)>0:
        msg='exist'
    else:
        msg='not_exist'
    return JsonResponse({'valid':msg})

def sendMessage(request):
    sender=request.session['id']
    status=['pending','deleted by receiver']
    msg_db=MessageModel.objects.filter(Sender_id=sender,Status__in=status)
    return render(request,'viewSendmessage.html',{'view':msg_db})

def deletemsg(request,id):
    
    msg_db=MessageModel.objects.filter(id=id)
    status=msg_db[0].Status
    if status== 'deleted by receiver':
        msg_db=MessageModel.objects.filter(id=id).delete()
        return redirect('sendMessage')
    else:
        msg_db=MessageModel.objects.filter(id=id).update(Status="deleted by Sender")
        return redirect('sendMessage')

def Userinbox(request):
    receiver=request.session['id']
    status=['pending','deleted by sender']
    # before applying filter
    # msg_db=MessageModel.objects.filter(Receiver_id=receiver).exclude(id__in=TrashModel.objects.filter(Receiver_id=receiver).values('Message_id'))
    
    # after applying filter
    agefactor_db=CustomerAgeFactorModel.objects.filter(User_id=receiver)
    for factor in agefactor_db:
        msg=MessageModel.objects.filter(Receiver=receiver,Filter_status='pending',Message__icontains=factor.Factor.Factor).exclude(Sender_id__in=BlackListModel.objects.filter(User=receiver).values('Contact')).update(Filter_status='Filtered')
        # print(factor.Factor.Factor_Name)
    
    customerhobbey_db=CustomerHobbyModel.objects.filter(User_id=receiver)
    for hobby in customerhobbey_db:
        hobbies=MessageModel.objects.filter(Receiver=receiver,Filter_status='pending',Message__icontains=hobby.Factor.Factor_Name).exclude(Sender_id__in=BlackListModel.objects.filter(User_id=receiver).values('Contact_id')).update(Filter_status='Filtered')

        print(hobby.Factor.Factor_Name)

    season_db=CustomerSeasonCountryModel.objects.filter(User_id=receiver)
    for season in season_db:
        seasons=MessageModel.objects.filter(Receiver=receiver,Filter_status='pending',Message__icontains=season.Factor.Factor_Name).exclude(Sender_id__in=BlackListModel.objects.filter(User_id=receiver).values('Contact_id')).update(Filter_status='Filtered')
        print(season.Factor.Factor_Name)

    contact_db=ContactModel.objects.filter(User=receiver)
    for contact in contact_db:
        contacts=MessageModel.objects.filter(Receiver=receiver,Filter_status='pending',Sender_id=contact.Contact).update(Filter_status='Filtered')
    msg_db=MessageModel.objects.filter(Receiver=receiver,Status__in=status,Filter_status='Filtered').exclude(id__in=TrashModel.objects.filter(Receiver=receiver).values('Message_id'))




    return render(request,'Userinbox.html',{'inbox':msg_db})

def msgTrash(request):
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    box=request.POST.getlist('checkbox')
    for cb in box:
        msg=MessageModel.objects.get(id=cb)
        receiver=request.session['id']
        trash_db=TrashModel(Date=date,Time=time,Message=msg,Receiver_id=receiver)
        trash_db.save()
    return render(request,'Userinbox.html')


def viewTrash(request):
    receiver=request.session['id']
    trash_db=TrashModel.objects.filter(Receiver_id=receiver)
    return render(request,'trash.html',{'trash':trash_db})


def deleteMessage(request,id):
    trash_db=TrashModel.objects.filter(id=id)
    msg_db=MessageModel.objects.filter(id=trash_db[0].Message_id)
    status=msg_db[0].Status
    if status == 'pending':
        update=MessageModel.objects.filter(id=trash_db[0].Message_id).update(Status="deleted by receiver")
        update2=TrashModel.objects.filter(id=id).delete()
        return redirect('viewTrash')

    else :
        status== 'deleted by sender'
        update=MessageModel.objects.filter(id=trash_db[0].Message_id).update(Status="Message deleted")        
        update2=TrashModel.objects.filter(id=id).delete()

        return redirect('viewTrash')


def forwardMessage(request,id):
    msg_db=MessageModel.objects.filter(id=id)
    return render(request,'forwardMessage.html',{'view':msg_db})

def forwardMessageAction(request):
    sender=request.session['id']
    receiver=request.POST['recname']
    rev=UserRegistrationModel.objects.get(Username=receiver)
    print(rev)
    subject=request.POST['subject']
    message=request.POST['message']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    msg_db=MessageModel(Subject=subject,Message=message,Date=date,Time=time,Receiver=rev,Sender_id=sender)
    msg_db.save()
    messages.add_message(request,messages.INFO,"Message forwarded")
    return redirect('Userinbox')

def replayMessage(request,id):
    msg_db=MessageModel.objects.filter(id=id)
    return render(request,'replayMessage.html',{'view':msg_db})

def replayMessageAction(request):
    sender=request.session['id']
    receiver=request.POST['name']
    rec=UserRegistrationModel.objects.get(Username=receiver)
    subject=request.POST['subject']
    message=request.POST['remsg']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    msg_db=MessageModel(Subject=subject,Message=message,Date=date,Time=time,Receiver=rec,Sender_id=sender)
    msg_db.save()
    messages.add_message(request,messages.INFO,"Replaied")
    return redirect('Userinbox')

def contact(request):
    return render(request,'contact.html')

def contactAtion(request):
    user=request.session['id']
    contact=request.POST['contact']
    con=UserRegistrationModel.objects.get(Username=contact)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    contact_db=ContactModel(Name=name,Date=date,Time=time,Contact=con,User_id=user,Remarks=remarks)
    contact_db.save()
    messages.add_message(request,messages.INFO,"Added to contact")
    return redirect('contact')


def contactView(request):
    user=request.session['id']
    contact_db=ContactModel.objects.filter(User_id=user)
    return render(request,'viewContact.html',{'con':contact_db})

def deleteContact(request,id):
    contact_db=ContactModel.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Contact deleted Succesfully")

    return redirect('contactView')

def blacklistContact(request):
    return render(request,'blacklist.html')

def blacklistContactAction(request):
    user=request.session['id']
    contact=request.POST['contact']
    con=UserRegistrationModel.objects.get(Username=contact)
    name=request.POST['name']
    remarks=request.POST['remarks']
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    blacklist_db=BlackListModel(Remarks=remarks,Name=name,Date=date,Time=time,Contact=con,User_id=user)
    blacklist_db.save()
    messages.add_message(request,messages.INFO,"Contact Added to blacklist")

    return redirect('blacklistContact')

def viewBlacklist(request):
    user=request.session['id']
    blacklist_db=BlackListModel.objects.filter(User_id=user)
    return render(request,'viewBlacklist.html',{'view':blacklist_db})



def deleteBlacklist(request,id):
    blacklist_db=BlackListModel.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"deleted Successfully")

    return redirect('viewBlacklist')

def blacklistContactMove(request,id):
    user=request.session['id']
    print(user)
    contact=ContactModel.objects.filter(id=id)
    contact_id=contact[0].Contact
    name=contact[0].Name
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")
    remarks=contact[0].Remarks
    blacklist_db=BlackListModel(Remarks=remarks,Name=name,Date=date,Time=time,Contact=contact_id,User_id=user)
    blacklist_db.save()
    contact.delete()
    return redirect('viewBlacklist')

def customerFactor(request):
    user=request.session['id']
    user_db=UserHobbyModel.objects.filter(User_id=user)
    return render(request,'CustomerFactor.html',{'factor':user_db})

def gethobby(request):

    hobb=request.GET['hobby']
    hobby_db=HobbyFactorModel.objects.filter(Hobby_id=hobb)
    return render(request,'getcustomerfactor.html',{'hobbies':hobby_db})

def customerHobby(request):
    user=request.session['id']
    # print(user)
    hobby=request.POST['hobby']
    # print(hobby)
    factor=request.POST['factor']
    # print(factor)
    customerhobby_db=CustomerHobbyModel(Factor_id=factor,Hobby_id=hobby,User_id=user)
    customerhobby_db.save()
    return render(request,'CustomerFactor.html')




def ageFactor(request):
    user=request.session['id']
    user_db=UserRegistrationModel.objects.filter(id=user)
    birthdate=user_db[0].DOB
    year=birthdate.split('-')
    old_year=year[0]
    date=datetime.date.today()
    birthyear=date.year
    age=int(birthyear)-int(old_year)
    age_db=AgefactorModel.objects.filter(Min_age__lte = age, Max_age__gte=age)
    return render(request,'customerAgeFactor.html',{'ages':age_db})

def ageFactorAction(request):
    user=request.session['id']
    factor=request.POST['factor']
    age_db=CustomerAgeFactorModel(Factor_id=factor,User_id=user)
    age_db.save()
    return redirect('ageFactor')


def customerSeason(request):
    user=request.session['id']
    user_db=UserRegistrationModel.objects.filter(id=user)
    country=user_db[0].Country
    print(country)
    state=user_db[0].State
    print(state)
    date=datetime.date.today()
    month=date.month
    print(month)
    season_db=SeasonCountryModel.objects.filter(Country=country,State=state,Months=month)
    print(season_db)
    return render(request,'customerSeasonfactor.html',{'season':season_db})

def customerSeasonAction(request):
    user=request.session['id']
    factor=request.POST['factor']
    seasoncountry_db=CustomerSeasonCountryModel(Factor_id=factor,User_id=user)
    seasoncountry_db.save()
    return redirect('customerSeason')

def viewSpam(request):
    user=request.session['id']
    
    status=['pending','deleted by sender']
    msg_db=MessageModel.objects.filter(Receiver=user,Status__in=status,Filter_status='pending')
    return render(request,'spamMessage.html',{'msg':msg_db})


def deleteSpam(request,id):
    # sender=request.session['id']
    user_db=MessageModel.objects.filter(id=id)
    status=user_db[0].Status
    if status == 'deleted by Sender':
        msg_db=MessageModel.objects.filter(id=id).delete()
        return redirect('viewSpam')
    else:
        msg_db=MessageModel.objects.filter(id=id).update(Status='deleted by receiver')
        return redirect('viewSpam')

    
def Editprofile(request):
    user=request.session['id']
    user_db=UserRegistrationModel.objects.filter(id=user)
    country_db=CountryModel.objects.all()
    state_db=StateModel.objects.all()
    hobbyname_db=HobbyModel.objects.all()
    hobby_db=UserHobbyModel.objects.filter(User=user)
    return render(request,'userEdit.html',{'view':user_db,'state':state_db,'countries':country_db,'hobbies':hobby_db,'hby':hobbyname_db})

def getstate(request):
    cid=request.GET['country']
    state_db=StateModel.objects.filter(Country=cid)
    return render(request,'getstate.html',{'state':state_db})
    



def editprofileAction(request):
    user=request.session['id']
    user1=UserRegistrationModel.objects.get(id=user)
    name=request.POST['name']
    dob=request.POST['dob']
    gender=request.POST['gender']
    address=request.POST['address']
    phone=request.POST['phone']
    question=request.POST['question']
    answer=request.POST['answer']
    country=request.POST['country']
    state=request.POST['state']
    username=request.POST['username']
    password=request.POST['password']
    user_db=UserRegistrationModel.objects.filter(id=user).update(Name=name,DOB=dob,Gender=gender,Address=address,Phone=phone,Security_question=question,Answer=answer,Country=country,State=state,Username=username+'@mymail.com',Password=password)
    hobby_db=UserHobbyModel.objects.filter(User=user).delete()
    hobby=request.POST.getlist('hobby')
    print(hobby)
    for h in hobby:
        hb=HobbyModel.objects.get(id=h)
        # print(hb)
        hobby_db=UserHobbyModel(Hobbies=hb,User=user1)
        hobby_db.save()
    messages.add_message(request,messages.INFO,"updated Successfully")
    return redirect('Editprofile')


        



   
    







    



