from django.shortcuts import render
from .models import Intro, Skill, SocialAccount, Project

def home(request):
    intro = Intro.objects.get(pk=2)
    skills = Skill.objects.all()
    socialaccounts = SocialAccount.objects.all()
    projects = Project.objects.all()

    ctx = {
        'intro': intro,
        'skills': skills,
        'socialaccounts': socialaccounts,
        'projects': projects,
    }
    return render(request, 'index.html', ctx)