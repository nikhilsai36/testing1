from django.urls import path
from .views import *

classurls =  [
    path('classapi/', StudentAPI.as_view()),
    path('classapi/<int:id>/', StudentAPI.as_view())
]