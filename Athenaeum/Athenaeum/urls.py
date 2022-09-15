"""Athenaeum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from THELIBRARY import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
router=DefaultRouter()
router.register("api/v4/books",views.BookViewSets,basename="Library")
router.register("api/v4/accounts/register",views.UserRegister,basename="registration")
router.register("api/v4/carts",views.CartsView,basename="carts")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/token",TokenObtainPairView.as_view()),
    path("api/v1/token/refresh",TokenRefreshView.as_view()),
    path("Library/",include("library.urls"))
]
