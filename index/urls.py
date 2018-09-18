from django.urls import path

from . import views

app_name='index'

urlpatterns = [
    path('', views.index, name='index'),
    path('form',views.form,name='form'),
    path('result',views.main,name='result'),
    path('model_info',views.model_info,name='model_info'),
    path('about_us',views.about_us,name='About Us'),
]