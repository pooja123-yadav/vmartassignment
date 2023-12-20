from django.urls import path
import apps.users.views as user_views

urlpatterns = [
    path("signup/", user_views.CreateUser.as_view(), name='signup-user'),
    path("login/", user_views.LoginUser.as_view(), name='login-user'),
    path("logout/", user_views.LogoutUser.as_view(), name='logout-user'),
    path("update-profile/", user_views.UpdateUser.as_view(), name='update-profile'),
]
