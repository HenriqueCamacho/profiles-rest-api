from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name="hello-viewset")#It will define all 4 urls for us

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #Convert api view class to be rendered by url's
    path("", include(router.urls)) #Generate a list of URL's that are associate with the viewset. INCLUDE will include multiple URL's at the same time
]