"""healthcareLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^new/', views.new_sample, name="new sample"),
    url(r'^registrationReceipt/', views.sample_registration_receipt, name="sample registration receipt"),
    url(r'^search/', views.search_sample, name="search sample"),
    url(r'^info/', views.sample_info, name="sample info"),
    url(r'^edit/', views.edit_sample, name="edit sample"),
    url(r'^update/', views.update_sample, name="update sample"),
    url(r'^delete/', views.delete_sample, name="delete sample"),
]
