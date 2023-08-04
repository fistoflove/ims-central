from django.http import HttpResponse
from django.template import loader
from .models import Website, MaintenanceTaskList, MaintenanceTask, WebsiteEvent, MaintenanceGrade
from .forms import MaintenanceForm
from datetime import datetime, date

import json

def index(request):
    websites = Website.objects.all()
    a_websites = Website.objects.filter(maintenance_grade=1)
    b_websites = Website.objects.filter(maintenance_grade=2)
    c_websites = Website.objects.filter(maintenance_grade=3)
    d_websites = Website.objects.filter(maintenance_grade=4)
    template = loader.get_template("maintenance/index.html")

    breadcrumbs = [
        {
            "icon": "fas fa-home",
            "title": "Home",
            "link": "/maintenance/"
        }
    ]

    context = {
        "total_websites": websites.count(),
        "a_websites": a_websites.count(),
        "b_websites": b_websites.count(),
        "c_websites": c_websites.count(),
        "d_websites": d_websites.count(),
        "breadcrumbs": breadcrumbs
    }
    return HttpResponse(template.render(context, request))

def websites_view(request):
    websites = Website.objects.all()

    template = loader.get_template("maintenance/website-list.html")
    website_list = []
    breadcrumbs = [
        {
            "icon": "fas fa-home",
            "title": "Home",
            "link": "/maintenance/"
        },
                {
            "icon": "fa-solid fa-globe",
            "title": "Websites",
            "link": "#",
        }
    ]

    for website in websites:
        website_list.append({
            "name": website.name,
            "url": website.url,
            "plan": website.maintenance_plan.name,
            "grade": website.maintenance_grade.name,
            "dsm": website.days_since_maintenance()
        })

    context = {
        "table_data": json.dumps(website_list, default=list),
        "website_list": websites,
        "request": request,
        "breadcrumbs": breadcrumbs
    }


    return HttpResponse(template.render(context, request))

def detail(request, website_id):
    website = Website.objects.get(id=website_id)
    events = WebsiteEvent.objects.filter(website=website)
    template = loader.get_template("maintenance/details.html")

    breadcrumbs = [
        {
            "icon": "fas fa-home",
            "title": "Home",
            "link": "/maintenance/"
        },
                {
            "icon": "fa-solid fa-globe",
            "title": "Websites",
            "link": "/maintenance/websites/",
        },
        {
            "icon": "fa-solid fa-circle-info",
            "title": website.name + " Details",
            "link": "/maintenance/websites/",
        }
    ]

    context = {
        "website": website,
        "website_events": events.order_by('-created_at').values(),
        "breadcrumbs": breadcrumbs
    }
    return HttpResponse(template.render(context, request))

def maintenance(request, website_id):
    website = Website.objects.get(id=website_id)
    grades = MaintenanceGrade.objects.all()
    if request.method == "POST":
        form = MaintenanceForm(request.POST)
        context = {
            "form": form
        }
        template = loader.get_template("maintenance/maintenance-complete.html")

        if form.is_valid():
            event = WebsiteEvent(
                name="maintenance",
                website=website,
                worker=request.user,
                data=form.data['task_data']
            )
            event.save()
            print(event.created_at)
            return HttpResponse(template.render(context, request))
    else:
        tasks = MaintenanceTask.objects.filter(task_list=website.maintenance_task_list)
        template = loader.get_template("maintenance/maintenance-form.html")
        context = {
            "website": website,
            "form": MaintenanceForm(),
            "tasks": tasks,
            "grades": grades
        }
    return HttpResponse(template.render(context, request))

def test(request):
    websites = Website.objects.filter(maintenance_grade=4)

    context = {}

    template = loader.get_template("maintenance/test.html")

    return HttpResponse(template.render(context, request))
