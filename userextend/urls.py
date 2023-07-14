from django.urls import path

from userextend import views

urlpatterns = [
    path('creare_user/', views.UserCreateView.as_view(), name='creare-user')
]