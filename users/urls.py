from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'^room', views.home,name='room-home'),
    path('',views.home,name='home'),

]