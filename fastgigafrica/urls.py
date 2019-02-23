"""fastgigafrica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('digitalmarket/', include('digitalmarket.urls')),
    path('educationwriting/', include('educationwriting.urls')),
    path('graphicdesign/', include('graphicdesign.urls')),
    path('programming/', include('programming.urls')),
    path('techbusiness/', include('techbusiness.urls')),
    path('videoanimation/', include('videoanimation.urls')),
    path('orderpay/', include('orderpay.urls')),
    # path('offerapost/', include('offerapost.urls')),
    # path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
