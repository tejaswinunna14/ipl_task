from django.urls import path
from rcb.views import *
app_name='something'
urlpatterns=[
    path('kingkohli/',kingkohli,name='kingkohli'),
]