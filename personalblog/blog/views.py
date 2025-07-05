from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User

def guest_home(request):
    return render(request, "guest/home.html")


@login_required
def admin_dashboard(request):
    ctx = {
        "total_users": User.objects.count(),
        "recent_signups": User.objects.order_by("-date_joined")[:5],
    }
    return render(request, "admin/dashboard.html", ctx)