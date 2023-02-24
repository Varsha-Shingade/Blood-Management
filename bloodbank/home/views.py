from django.shortcuts import render,HttpResponse
from home.models import Donar
from home.models import Recipient

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def registration(request):
    return render(request,'registration.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def donar(request):
    if request.method=='POST':
        firstname=request.POST.get('First_Name')
        lastname=request.POST.get('Last_Name')
        age=request.POST.get('age')
        email=request.POST.get('Email_Id')
        pno=request.POST.get('Mobile_Number')
        gender=request.POST.get('gender')
        isftd=request.POST.get('Is this your first time donating?')
        bloodgroup=request.POST.get('Blood Group')
        address=request.POST.get('Address')
        city=request.POST.get('City')
        pincode=request.POST.get('Pin_Code')
        state=request.POST.get('State')
        donar=Donar(firstname=firstname,lastname=lastname,age=age,email=email,pno=pno,gender=gender,isftd=isftd,bloodgroup=bloodgroup,address=address,city=city,pincode=pincode,state=state)
        donar.save()
    return render(request,'donar.html')
def recipient(request):
    if request.method=='POST':
        firstname=request.POST.get('First_Name')
        lastname=request.POST.get('Last_Name')
        age=request.POST.get('age')
        email=request.POST.get('Email_Id')
        pno=request.POST.get('Mobile_Number')
        gender=request.POST.get('gender')
        bloodgroup=request.POST.get('Blood Group')
        address=request.POST.get('Address')
        city=request.POST.get('City')
        pincode=request.POST.get('Pin_Code')
        state=request.POST.get('State')
        recipient=Recipient(firstname=firstname,lastname=lastname,age=age,email=email,pno=pno,gender=gender,bloodgroup=bloodgroup,address=address,city=city,pincode=pincode,state=state)
        recipient.save()
    return render(request,'recipient.html')
def alldonars(request):
    return render(request,'alldonars.html')
def allrecipients(request):
    return render(request,'allrecipients.html')


