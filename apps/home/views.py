from django.shortcuts import render
from apps.home.models import Home, Service, Price, Partners, Team, FAQ, Contact
from apps.home.forms import ContactForm

# Create your views here.
def index(request):
    home = Home.objects.latest('id')
    service = Service.objects.all().order_by('-id')[:3]
    price = Price.objects.all().order_by('-id')[:3]
    partners = Partners.objects.all().order_by('-id')
    teams = Team.objects.all().order_by('-id')
    faq = FAQ.objects.all().order_by('-id')
    context = {
        'homes' : home,
        'prices' : price,
        'services' : service,
        'partners' : partners,
        'teams' : teams,
        'faqs' : faq,
    }
    return render(request, 'index.html', context)

def service(request):
    home = Home.objects.latest('id')
    context = {
        'homes' : home,
    }
    return render(request,'services.html',context)
    
def contact_us(request):
    context={}
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form    
    return render(request,'contact-us.html', context)    

def thank_you(request):
    return render (request,'thank_you.html')


def support(request):
    contact = Contact.objects.all()
    home = Home.objects.latest('id')
    context = {
        'contacts' : contact,
        'homes' : home,
    }
    return render(request,'support.html',context) 

def about_us(request):
    home = Home.objects.latest('id')
    partners = Partners.objects.all().order_by('-id')
    teams = Team.objects.all().order_by('-id')
    context = {
        'homes' : home,
        'partners' : partners,
        'teams' : teams,
    }
    return render (request, 'about-us.html',context)   

def service_detail(request, id):
    service = Service.objects.get(id = id)
    context = {
        'service' : service
    }
    return render(request, 'service-details.html', context)