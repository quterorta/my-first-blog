"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
from .views import NewsViewSet

#router = SimpleRouter()
#router.register(r'search', NewsViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('social', views.social, name='social'),
    path('guides', views.guides, name='guides'),
    path('culture', views.culture, name='culture'),
    path('lifestyle', views.lifestyle, name='lifestyle'),
    path('sex-and-love', views.sex_and_love, name='sex-and-love'),
    path('post/<str>/<int:id>', views.PostDetailView.as_view(), name='post-detail'),
    path('search/', views.Search.as_view(), name='search'),
    path('cookies', views.cookie, name='cookie'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
    path('terms-of-use', views.terms_of_use, name='terms-of-use'),
]

# urlpatterns += router.urls

