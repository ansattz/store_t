from django.shortcuts import render
from django.http import HttpResponse
from .models import Type
from .models import Announcement

def home(request):
   types = Type.objects.all()
   announcements = Announcement.objects.all()

   return render(request, 'home.html', {'types': types, 'announcements': announcements})
