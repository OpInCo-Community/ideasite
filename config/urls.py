"""config URL Configuration

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
from django.contrib.auth.views import LoginView, LogoutView

from ideas import views as ideas_views
from core import views as core_views
ideas_patterns = [
    # path("create/", ideas_views.create_view, name="create"),
    # path("idea/<slug:slug>/", ideas_views.detail_view, name="detail"),
    path("idea/like/<int:idea_pk>", ideas_views.like, name="like"),
    path("", ideas_views.home, name="home"),

]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("profile/", core_views.profile, name="profile"),
    path("", include((ideas_patterns, 'ideas')))
]

