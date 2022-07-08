from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Type
from .models import Announcement

def home(request):
   types = Type.objects.all()
   last_announc = Announcement.objects.all()[:12]

   return render(request, 'home.html', {'types': types,
                                       'announcements': last_announc})


def type(request, type_id):
   types = Type.objects.all()

   type = get_object_or_404(Type, id=type_id)
   announcements = Announcement.objects.filter(type=type)

   return render(request, 'home.html', {'types': types,
                                       'announcements': announcements,
                                       'type': type })


def announcement(request, announcement_id):
   announcement = get_object_or_404(Announcement, id=announcement_id)

   types = Type.objects.all()

   return render(request, 'announcement.html', {'types': types,
                                       'announcement': announcement})


