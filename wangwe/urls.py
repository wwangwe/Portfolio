from django.urls import path
from .views import index

app_name = 'wangwe'
urlpatterns = [
    path('', index, name='home'),
]
