from django.urls import path

from . import views

#create the url
urlpatterns = [
    path('', views.home, name="home_page"),
    path('user/', views.user_form, name="user_page"),
    path('partner/', views.partner_form, name="partner_page"),
]