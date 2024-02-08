from django.shortcuts import render
from . models import Course, Team, Testimonial, Contact

# Create your views here.
def notfound(request):
    return render(request, "web/404.html")

def about(request):
    context = {
        'team': Team.objects.all()
    }
    return render(request, "web/about.html", context)

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact1 = Contact(
            name=name,
            email=email,            
            subject=subject,
            message=message
        )

        contact1.save()
    return render(request, "web/contact.html")

def courses(request):
    context = {
        'course': Course.objects.all(),
        'testimonial': Testimonial.objects.all()
    }
    return render(request, "web/courses.html", context)

def index(request):
    context = {
        'course': Course.objects.all(),
        'team': Team.objects.all(),
        'testimonial': Testimonial.objects.all()
    }
    return render(request, "web/index.html", context)

def team(request):
    context = {
        'team': Team.objects.all()
    }
    return render(request, "web/team.html", context)

def testimonial(request):
    context = {
        'testimonial': Testimonial.objects.all()
    }
    return render(request, "web/testimonial.html", context)