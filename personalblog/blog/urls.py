from django.urls import path
from . import views

urlpatterns = [
    path("",views.guest_home, name="guest-home"),
    path("dashboard/",views.admin_dashboard, name="admin-dashboard")
]