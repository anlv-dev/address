from django.urls import path
from . import views
app_name = 'formpro'

urlpatterns = [
    path('', views.formView, name='formview'), 
]
