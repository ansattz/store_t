from django.urls import path
from .views import home
from .views import type
from .views import announcement


urlpatterns = [
    path('', home, name='home'),
    path('type/<int:type_id>', type, name='type'),
    path('announcement/<int:announcement_id>', announcement, name='announcement')
]