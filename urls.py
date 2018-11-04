from django.conf.urls import url, include
import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mix/', views.mix, name='mix'),
    url(r'^order/', views.order, name='order'),
    url(r'^cashbox/$', views.cashbox, name='cashbox'),
]
