from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("index/home.html")
    context = {
        "request": request
    }
    return HttpResponse(template.render(context, request))