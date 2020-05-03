"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
This version of the quickstart within the  django rest framework
seems to match django 1.11 syntax

https://github.com/encode/django-rest-framework/blob/e148637d6d15d07562e3588b86d9ba94314150e0/docs/tutorial/quickstart.md

"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from options_data import views as options_data_views
from quickstart import views as quickstart_views


router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'group', quickstart_views.GroupViewSet)
router.register(r'option', options_data_views.OptionRawDataViewSet, "option-general")
router.register(r'options/cme', options_data_views.CMEOptionRawDataViewSet, "options-cme")
router.register(r'options/ice', options_data_views.ICEOptionRawDataViewSet, "options-ice")
router.register(r'options/eurex', options_data_views.EUREXOptionRawDataViewSet, "options-eurex")
router.register(r'options/usetf', options_data_views.USETFOptionRawDataViewSet, "options-usetf")



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
