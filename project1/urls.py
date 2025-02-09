"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views import *
from zomato.views import *
from swiggy.views import *
from blinkit.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kiran/', kiran, name='kiran'),
    path('sagar/',sagar, name='sagar'),
    path('hello/', hello, name='hello'),
    path('youtube/',youtube, name='youtube'),
    path('form/',form,name='form'),
    path('welcome/',welcome, name='welcome'),
    path('zomato/',zomato, name='zomato'),
    path('welcomeswiggy/',welcomeswiggy,name='welcomeswiggy'),
    path('swiggy/',swiggy, name='swiggy'),
    path('welcomeblinkit/',welcomeblinkit,name='welcomeblinkit'),
    path('blinkit/',blinkit,name='blinkit')
]