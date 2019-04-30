from django.urls import path
from . import views

urlpatterns=[
    path('filled/',views.filled,name='filled'),
    path('congratulation/',views.congratulation,name='congratulation'),
]


