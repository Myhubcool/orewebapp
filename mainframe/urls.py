from django.urls import path
from . import views

urlpatterns = [
    path('',views.homee,name='homee'),
    path('loggedin/',views.home,name='home'),
    path('mnframe/',views.mnframe,name='mnframe'),
    path('tservice',views.tservice,name='tservice')
]
