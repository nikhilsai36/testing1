from .views import *
from django.urls import path

urlpatterns = [
    path('details/', details),
    path('create/', create),
    path('update/<int:id>/', update),
    path('delete/<int:id>/', dele),
    path('studetails/', studetails),
    path('stucreate/', stucreate),
    path('stuupdate/<int:id>/', stuupdate),
    path('studelete/<int:id>/', studelete),
]
# details
# create
# update
# delete1