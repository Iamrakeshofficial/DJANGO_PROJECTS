from django.urls import path

from .import views

urlpatterns=[
    path('/show',views.add_Details,name='show'),
    path('/wel',views.Welcome,name='wel'),
]