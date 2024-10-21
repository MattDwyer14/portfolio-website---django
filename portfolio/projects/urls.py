from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.base, name='base'),
    #path('<int:id>', views.detail, name='detail')
]
