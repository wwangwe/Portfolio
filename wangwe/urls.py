from django.urls import path
from .views import index, resume

app_name = 'wangwe'
urlpatterns = [
    path('', index, name='home'),
    path('resume/', resume, name='resume')
]
