"""backend_assignment URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import ObtainAuthToken
from paragraphs.views import ParagraphCreateView, ParagraphSearchView, UserCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', ObtainAuthToken.as_view()),
    path('api/paragraphs/', ParagraphCreateView.as_view(), name='paragraph-create'), # POST
    path('paragraphs/search/', ParagraphSearchView.as_view(), name='paragraph-search'), # GET
    path('api/users/', UserCreateView.as_view(), name='user-create'), # POST
    # Include other paths as needed
]



