from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name="home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',views.login_view,name="login"),
    path('register/',views.registerView,name="register"),
    path('logout/',LogoutView.as_view(next_page='home'),name="logout"),
]