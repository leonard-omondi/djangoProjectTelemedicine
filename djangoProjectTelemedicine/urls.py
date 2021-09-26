"""djangoProjectTelemedicine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('telemedicine/', include('telemedicine.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from patient import views as patient_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', patient_view.register, name='register'),
    path('profile/', patient_view.profile, name='profile'),
    path('patient/', patient_view.patient, name='patient'),
    path('', include('telemedicine.urls')),  # Empty path makes this our homepage
    path('login/', auth_views.LoginView.as_view(template_name='patient/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='patient/logout.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
