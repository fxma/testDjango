"""testDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from testDjango.views import *
from . import views,testdb,search

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.hello),
    url(r'^hello/$', hello),
    path('current_time/', current_time),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^testdb/$', testdb.testdb),
    path('querydb/', testdb.querydb),
    path('updatedb/', testdb.updatedb),
    path('deletedb/', testdb.deletedb),
    url(r'^search_form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search_post/$', search.search_post),

]