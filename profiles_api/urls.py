from django.urls import path

from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()) #Convert api view class to be rendered by url's
]