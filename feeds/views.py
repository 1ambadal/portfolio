from django.shortcuts import render
from .models import *
from django.http import FileResponse
# Create your views here.


def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myskills = Projects.objects.all()
    skills = Skills.objects.all()
    blogs = Blogs.objects.all()
    contact = Contact.objects.all()
    context = {
        "info": myinfo,
        "about": myabout,
        "work": myskills,
        "skills": skills,
        "blogs":blogs,
        "contact":contact,
    }

    return render(request, 'home_page.html', context)


def resume(request):
    filepath = './media/images/resume.pdf' 
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')