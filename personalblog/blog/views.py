from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, You are welcome to write your blogs.")