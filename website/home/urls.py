from django.conf.urls import url
from . import views
app_name='home'

urlpatterns = [
url(r'^$', views.Home.as_view(), name = 'home'),
url(r'^heart/', views.check_heartSymptom, name = 'heart'),
url(r'^diabetes/', views.check_diabSymptom, name = 'diabetes')
]
