"""empmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from employee.admin import custom_admin_site
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('', include('accounts.urls')),
    path('ems/', include('employee.urls')),
    # Add this to handle Django's built-in auth URLs
    path('accounts/login/', RedirectView.as_view(url='/')),  # Redirect to our custom login
    path('accounts/', include('django.contrib.auth.urls')),
]

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This is for production (works with WhiteNoise)
# No need to serve static files in production as WhiteNoise handles them
# But we still need to serve media files in production
if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
