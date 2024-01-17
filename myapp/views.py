from django.shortcuts import render
from .models import Customer , Service , Banner , Social_medias , TeamMember
# Create your views here.
def index (request):
    banner = Banner.objects.all()
    context = {
        'banner' : banner,
    }
    return render(request , 'index.html' , context )

def about (request,social_media_id):
    social_media = Social_medias.objects.filter( id = social_media_id)
    context = {
        'social_media' : social_media
    }
    return render(request , 'about.html' , context )


def service (request , customer_id):
    service = Service.objects.filter( id = customer_id)
    contex = {
        'service' : service
    }
    return render(request , 'service.html' , contex )


def team (request , teammember_id):
    team = TeamMember.objects.filter( id = teammember_id)
    context = {
        'context' : context
    }
    return render(request , 'team.html' , context )

def why (request):
    customer = Customer.objects.all()
    context = {
        'customer' : customer
    }
    return render(request , 'why.html' , context )