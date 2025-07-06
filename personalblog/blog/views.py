from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Article
from django.urls import reverse
from django.http import HttpResponseRedirect

def guest_home(request):
    return render(request, "guest/home.html")


@login_required
def admin_dashboard(request):
    list_articles = Article.objects.all().order_by("created_at")
    # ctx = {
    #     "total_users": User.objects.count(),
    #     "recent_signups": User.objects.order_by("-date_joined")[:5],
    # }
    display_article = {
        "total_articles":Article.objects.count(),
        "list_articles": list_articles,
    }
    return render(request, "admin/dashboard.html",display_article)

def goodbye(request):
    """
    Do any post-logout cleanup, then punt the user to the real logout view.
    """
    logout_url = reverse("logout")
    return HttpResponseRedirect(logout_url)