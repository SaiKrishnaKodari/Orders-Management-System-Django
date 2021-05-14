"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,re_path,include
from myapp1 import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/',views.index),
   # path('',views.not_logged),
    path('',views.not_logged),
    path('login/',views.login_view),
    path('logout/',views.logout_view),
    path('bookings/',views.viewjob),
    path('add/',views.addjob),
    path('tasks/',views.viewjob),
    path('customers/',views.clientspage),
    path('brands/',views.brands),
    path('Employees/',views.employees),
    re_path(r'^(?P<selfid>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', views.track),
    re_path(r'^bookings/parts/(?P<id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', views.parts),
    re_path(r'^bookings/status/(?P<id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', views.edit),
    re_path(r'^bookings/mail/(?P<id>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})', views.mail),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)