from django.shortcuts import render
from django.http import HttpResponse
from .models import Type
from .models import Announcement

def home(request):
   types = Type.objects.all()
   last_announc = Announcement.objects.all()[:12]


   return render(request, 'home.html', {'types': types, 'announcements': last_announc})
