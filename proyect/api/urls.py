from django.urls import path
from .views import ElementView

urlpatterns =[
    path('elements/', ElementView.as_view(), name='elements_list'),
    path('elements/<int:id>', ElementView.as_view(), name = 'elements_process')
]