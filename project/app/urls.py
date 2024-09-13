from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('registration/',registration,name='registration'),
    path('login/',login,name='login'),
    path('delete/',delete,name='delete')
    
]
