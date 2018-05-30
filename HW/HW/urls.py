"""HW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('commodity/',views.commodity),
    path('commodity/insert/',views.insert),
    path('commodity/do_insert/',views.do_insert),
    path('commodity/do_update/',views.do_update),
    path('commodity/do_delete/',views.do_delete),
    path('commodity/update/<int:commodity_id>/',views.update),
    path('commodity/detail/<int:commodity_id>/',views.detail),
    path('commodity/delete/<int:commodity_id>/',views.delete),
    path('index2/',views.index2),
    path('index/',views.index),
    path('echo_once/',views.echo_once),
    path('echo/<int:userid>',views.echo),
]
