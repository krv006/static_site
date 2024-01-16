from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request , 'index.html' )

def about (request):
    return render(request , 'about.html' )


def service (request):
    return render(request , 'service.html' )


def team (request):
    return render(request , 'team.html' )



def why (request):
    return render(request , 'why.html' )