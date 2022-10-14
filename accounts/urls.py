from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:user_id>", views.detail, name="detail"),
    path("update/<int:user_id>", views.update, name="update"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
]
