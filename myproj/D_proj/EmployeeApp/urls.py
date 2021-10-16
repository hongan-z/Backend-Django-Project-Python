
from django.conf.urls import url
from django.urls.conf import path
from EmployeeApp import views

urlpatterns = [

  url(r'^department/$', views.deppartmentApi),
  url(r'^department/([0-9]+)$',views.deppartmentApi)

]