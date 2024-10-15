
from django.contrib import admin
from django.urls import path, include
from poesias.views import my_view , root_view , user_view , home , contexto , lois

urlpatterns = [
    path('home/', home),
    path('', root_view),
    path('sobre/', my_view),
    path('user/<str:username>/', user_view),
    path('contexto/', contexto, name='contexto'), 
    path('lois/', lois),
]
