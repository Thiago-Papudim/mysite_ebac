from django.urls import path

from mysite_ebac.blog import views

urlpatterns = [
    path('', views.PostView.as_view(), name='home')
]
