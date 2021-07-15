from django.shortcuts import render
from django.http import HttpResponse
from .models import customerentry,Mobilemodel,customer
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth import authenticate, login,logout
from barcode import EAN13
  
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return not_logged(request)
    else:
        return render(request,'main.html') 
    return render(request,'main.html')
  

def not_logged(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            # print(request.POST)
            value=request.POST.get("uuid")
            # print(value)
            tasks=customerentry.objects.filter(id=value)
            tasks=[obj.__dict__ for obj in tasks]
            # print(tasks)
            return render(request,"customer.html",{'tasks':tasks})
        return render(request,"customer.html")    
    else:
        return render(request,"main.html")             

def track(request,selfid):
    tasks=customerentry.objects.filter(id=selfid)
    tasks=[obj.__dict__ for obj in tasks]
    # print(tasks)
    return render(request,"customer.html",{'tasks':tasks})
                          
def logout_view(request):
    logout(request)
    return index(request)

def final(request):
    return render(request,"customerpage.html") 
def final2(request):
    return render(request,"index.html")   
  

def login_view(request):
    if request.method=="POST":
        # print(request.POST)
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            a=login(request,user)
            return index(request)
        else:
            return HttpResponse("invalid credentails")
        return HttpResponse("IN login post")

    return render(request,"logphp.html")        
def bookings(request):
    return render(request,'booking.html')
def addjob(request):
    # book_form=bookingform(request.POST)
    us=User.objects.all()
    techies=[techie.__dict__ for techie in us]
    brandss=Mobilemodel.objects.all()
    devices=[brand.__dict__ for brand in brandss]
    if request.method=="POST":
        obj=customerentry()
        client=customer()
        obj.Customername=request.POST['customer']
        client.Name=request.POST['customer']
        obj.Receivedate=request.POST["receive_date"]
        obj.Deliverydate=request.POST["delivery_date"]
        obj.jobpending=request.POST["technician"]
        obj.Email=request.POST['email']
        client.Email=request.POST['email']
        client.save()

        obj.devicebrand=request.POST["brand_id"]
        obj.devicemodel=request.POST["model"]
        obj.imei=request.POST["imeinumber"]
        obj.devicecolour=request.POST["color"]
        obj.providerinfo=request.POST["provider"]
        obj.password=request.POST["device_password"]

        obj.fault=request.POST["fault_discription"]
        obj.amount=request.POST["amount"]

        obj.power=request.POST["power_on"]
        obj.charging=request.POST["charging"]
        obj.display=request.POST["display"]
        obj.camera=request.POST["camera"]
        obj.battery=request.POST["battery"]

        obj.pictures=request.POST["snaps"]
        obj.others=request.POST["notes"]
        obj.save()
        # print(obj.id)
        unique=obj.id
        job=customerentry.objects.filter(id=unique)
        partsenter=[obj.__dict__ for obj in job]
        # print(partsenter[0])
        mail=list({partsenter[0]["Email"]})
        subject = 'welcome to Trubot world'
        message = f'Hi {partsenter[0]["Customername"]}, Thanks for visiting store,You can track your device by clicking below link."http://127.0.0.1:8000/{partsenter[0]["id"]}"'
        message.attach('logo.png', img_data, 'static/logo.png')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [mail[0]]
        send_mail( subject, message, email_from, recipient_list )
        # ////////////////////////////////////////////////
        msg = EmailMessage(subject,message, email_from, recipient_list)
        # ////////////////////////////////////////////////
        return render(request,'addjob.html',{"obj":unique})
    return render(request,'addjob.html',{'devices':devices,'techies':techies})    

def viewjob(request):
    # data=customerentry.objects.filter(jobpending=request.user.username)
    data=customerentry.objects.all().order_by('-status')
    bookings=[obj.__dict__ for obj in data]
    bookings=bookings[::-1]
    return render(request,'booking.html',{"bookings":bookings})

def parts(request,id):
    job=customerentry.objects.filter(id=id)
    partsenter=[obj.__dict__ for obj in job]
    if request.method=="POST":
        # job.parts=request.POST['partsrecord']
        customerentry.objects.filter(id=id).update(parts = request.POST['partsrecord'])
        return render(request,'parts.html',{'partsenter':partsenter}) 
    return render(request, "parts.html",{'partsenter':partsenter})     
def edit(request,id):
    customerentry.objects.filter(id=id).update(status = True)
    return mail(request,id)

def mail(request,id):
    job=customerentry.objects.filter(id=id)
    partsenter=[obj.__dict__ for obj in job]
    # print(partsenter[0])
    mail=list({partsenter[0]["Email"]})
    subject = 'welcome to Trubot world'
    message = f'Hi {partsenter[0]["Customername"]}, You are ready to pick up your Device.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [mail[0]]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'main.html')


def clientspage(request):
    data=customer.objects.all()
    bookingsclients=[obj.__dict__ for obj in data]
    bookingsclients=bookingsclients[::-1]
    return render(request,'clients.html',{'bookingsclients':bookingsclients})


def brands(request):
    if request.method=="POST":
        # print("in post")
        dev=Mobilemodel()
        dev.devicename=request.POST['brandname']
        dev.save()
        data=Mobilemodel.objects.all()
        deals=[obj.__dict__ for obj in data]
        deals=deals[::-1]
        return render(request,'brands.html',{'deals':deals})
    data=Mobilemodel.objects.all()
    # print("out if")
    deals=[obj.__dict__ for obj in data]
    deals=deals[::-1]
    return render(request,'brands.html',{'deals':deals})

def employees(request):
    data=User.objects.all().order_by('-id')
    emp=[obj.__dict__ for obj in data]
    emp=emp[::-1]
    return render(request,'employees.html',{'emp':emp})

def print(request,id):
    job=customerentry.objects.filter(id=id)
    invoice=[obj.__dict__ for obj in job]
    return render(request, "invoice.html",{'invoice':invoice,'count':'1'}) 

def checkin(request,id):
    job=customerentry.objects.filter(id=id)
    invoice=[obj.__dict__ for obj in job]
    return render(request, "checkin.html",{'invoice':invoice,'count':'1'}) 


def normal(request):
    subject = 'welcome to Trubot world'
    message = 'welcome to Trubot world mister'
    email_from = settings.EMAIL_HOST_USER
    msg = EmailMessage(subject,message, email_from,['saikrishnakodari00@gmail.com'])
    msg.attach_file('static/logo.png')
    msg.send()
    return HttpResponse('sent')