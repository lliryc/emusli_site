"""emusli_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from emusli import views
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView

class UserRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mix/', views.mix, name='mix'),
    url(r'^order/', views.order, name='order'),
    url(r'^cashbox/$', views.cashbox, name='cashbox'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register', UserRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
