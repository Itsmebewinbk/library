from django.urls import path
from library import views
urlpatterns=[
    path("signup",views.SignInView.as_view(),name="register"),
    path("login",views.LogInView.as_view(),name="signin"),
    path("home",views.IndexView.as_view(),name="index"),
    path("signout",views.SignOutView.as_view(),name="signout"),
]