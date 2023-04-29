"""
URL configuration for PerfTest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import PerfTest
import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/', views.upload_file, name='api_upload_file'),
    path('api/download/', views.download_file, name='api_download_file'),
    path('api/delete/', views.delete_file, name='api_delete_file'),
]
