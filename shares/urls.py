
from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("", views.index, name="index"),
    path("open", views.openPage, name="openPage"),

    path("news", views.news, name="news"),
    path("stocks", views.stocks, name="stocks"),
    path("stocks/<str:symbol>", views.stockinfo, name="stockinfo"),
    path("api/v1/open", views.open, name="open"),
    path("api/v1/close", views.close, name="close")
]