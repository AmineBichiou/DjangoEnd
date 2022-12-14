from django.urls import path
from . import views
urlpatterns = [
    path('', views.connect, name='connect'),
    path('login/', views.signIn, name='signIn'),
    path('login/login/', views.signIn, name='signIn'),
    path('disconnect/', views.signOut, name='disconnect'),
    path('test/', views.test, name='test'),
]